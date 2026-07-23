import streamlit as st
import pandas as pd
import os

from agents.restaurant_agent import RestaurantAgent
from agents.user_agent import UserAgent


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Restaurant AI Agent",
    page_icon="🍽️",
    layout="wide"
)


# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():

    file_path = os.path.join(
        "data",
        "clean_restaurants_dataset.csv"
    )

    df = pd.read_csv(file_path)

    return df


df = load_data()



# -----------------------------
# Load Agents
# -----------------------------
@st.cache_resource
def load_agents():

    restaurant_agent = RestaurantAgent()

    user_agent = UserAgent()

    return restaurant_agent, user_agent



restaurant_agent, user_agent = load_agents()



# -----------------------------
# Title
# -----------------------------
st.title("🍽️ Restaurant Recommendation AI Agent")

st.write(
    "AI powered restaurant recommendation system using RAG and multi-agent architecture."
)



# =====================================================
# NORMAL SEARCH SYSTEM
# =====================================================

st.header("🔎 Search Restaurants")


col1, col2 = st.columns(2)


with col1:

    location = st.selectbox(
        "Select Location",
        ["All"] + sorted(
            df["Location"].dropna().unique()
        )
    )


with col2:

    cuisine = st.selectbox(
        "Select Cuisine",
        ["All"] + sorted(
            df["Cuisine"].dropna().unique()
        )
    )


budget = st.selectbox(
    "Select Budget",
    ["All"] + sorted(
        df["Budget"].dropna().unique()
    )
)


min_rating = st.slider(
    "Minimum Rating",
    0.0,
    5.0,
    4.0
)



if st.button("🍴 Recommend Restaurants"):


    result = df.copy()


    if location != "All":

        result = result[
            result["Location"] == location
        ]


    if cuisine != "All":

        result = result[
            result["Cuisine"] == cuisine
        ]


    if budget != "All":

        result = result[
            result["Budget"] == budget
        ]


    result = result[
        pd.to_numeric(
            result["Rating"],
            errors="coerce"
        )
        >= min_rating
    ]



    if len(result) > 0:

        st.success(
            f"{len(result)} restaurants found"
        )


        for _, row in result.iterrows():

            st.subheader(
                row["Restaurant_Name"]
            )


            st.write(
                f"""
🍛 Cuisine: {row['Cuisine']}

📍 Location: {row['Location']}

💰 Budget: {row['Budget']}

⭐ Rating: {row['Rating']}

📝 Review: {row['Review']}
"""
            )

            st.divider()


    else:

        st.warning(
            "No restaurants found."
        )




# =====================================================
# AI CHATBOT
# =====================================================


st.header("💬 Chat With Restaurant AI")


question = st.text_input(
    "Ask anything about restaurants..."
)



if st.button("🤖 Ask AI"):


    if question.strip():


        with st.spinner(
            "AI Agent is thinking..."
        ):


            # User Agent receives user query

            preferences = user_agent.get_preferences(
                location="",
                cuisine="",
                budget="",
                rating=0
            )


            # Restaurant Agent handles RAG + Review + LLM

            answer = restaurant_agent.get_recommendation(
                question
            )


        st.subheader(
            "🤖 AI Recommendation"
        )


        st.write(answer)



    else:

        st.warning(
            "Please enter a question."
        )