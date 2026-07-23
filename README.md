# 🍽️ Restaurant Recommendation AI Agent

An AI-powered restaurant recommendation system developed using a **multi-agent architecture**, **Retrieval Augmented Generation (RAG)**, **FAISS vector search**, and **LLM-based reasoning**.

This system recommends suitable restaurants based on user preferences such as cuisine, location, budget, rating, and natural language queries.

---

## 📌 Project Overview

The Restaurant Recommendation AI Agent allows users to find restaurants in two ways:

### 1. Filter-Based Restaurant Search

Users can select:

- Location
- Cuisine
- Budget
- Minimum Rating

The system filters the restaurant dataset and displays matching restaurants.

### 2. AI Restaurant Chat Assistant

Users can ask questions naturally, and the AI agent provides recommendations.

Example queries:

- "Suggest seafood restaurants in Colombo"
- "Find budget-friendly Indian restaurants"
- "Which restaurant is best for a family dinner?"
- "Recommend highly rated restaurants"

The AI agent retrieves relevant restaurant information and generates personalized recommendations.

---

# 🏗️ System Architecture

```
                         User
                          |
                          |
                          v
                     User Agent
                          |
              Structured User Preferences
                          |
                          v
                 Restaurant Agent
                          |
              -------------------------
              |                       |
              v                       v
          RAG System            Review Agent
              |                       |
              v                       |
       FAISS Vector Search            |
              |                       |
              -----------+------------
                          |
                          v
                    LLM Agent
                          |
                          v
             Final Recommendation
```

---

# 🤖 Multi-Agent Architecture

## 1. User Agent

### Responsibility:

- Receives user requirements.
- Converts user inputs into structured preferences.
- Sends user information to the Restaurant Agent.

Example structured message:

```json
{
  "location": "Colombo",
  "cuisine": "Seafood",
  "budget": "High",
  "rating": 4.5
}
```

---

## 2. Restaurant Agent

### Responsibility:

- Works as the main orchestrator agent.
- Controls the recommendation workflow.
- Communicates with RAG, Review Agent, and LLM Agent.
- Retrieves relevant restaurants based on user queries.

---

## 3. Review Agent

### Responsibility:

- Analyzes restaurant ratings.
- Calculates recommendation scores.
- Sorts restaurants based on quality.

---

## 4. LLM Agent

### Responsibility:

- Generates final natural language responses.
- Explains recommendations.
- Provides user-friendly restaurant suggestions.

Language Model:

```
Llama-3.1-8B-Instant
```

Provider:

```
Groq
```

---

# 🔄 Agent-to-Agent Communication Flow

The system follows a multi-agent communication workflow:

```
User
 |
 | Restaurant Query
 |
 v
User Agent
 |
 | Structured Preferences
 |
 v
Restaurant Agent
 |
 | Retrieve Relevant Information
 |
 v
RAG System
 |
 | Restaurant Documents
 |
 v
Review Agent
 |
 | Ranked Restaurants
 |
 v
LLM Agent
 |
 | Generated Recommendation
 |
 v
User
```

---

# 🔎 Retrieval Augmented Generation (RAG)

The system uses RAG to improve recommendation accuracy by retrieving relevant restaurant information before generating responses.

## RAG Pipeline

```
Restaurant Dataset
        |
        v
Document Creation
        |
        v
Sentence Transformer Embeddings
        |
        v
FAISS Vector Database
        |
        v
Similarity Search
        |
        v
Relevant Restaurant Information
        |
        v
LLM Response Generation
```

---

# 📊 Dataset Information

The restaurant dataset contains:

- Restaurant Name
- Cuisine
- Location
- Budget
- Rating
- Review

The dataset is converted into documents and embedded using a sentence transformer model.

---

# 🧠 Model Selection Strategy

## Embedding Model

Model:

```
all-MiniLM-L6-v2
```

Reason:

- Lightweight embedding model.
- Fast processing.
- Suitable for small domain datasets.
- Requires less computational resources.

---

## Language Model

Model:

```
Llama-3.1-8B-Instant
```

Provider:

```
Groq
```

Reason:

- Low latency.
- Fast response generation.
- Good conversational performance.
- Suitable for real-time AI assistants.

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- FAISS
- Sentence Transformers
- Pandas
- NumPy
- GitHub

---

# 📂 Project Structure

```
Restaurant_Recommendation_System

│
├── agents
│   ├── user_agent.py
│   ├── restaurant_agent.py
│   ├── review_agent.py
│   └── llm_agent.py
│
├── rag
│   ├── create_documents.py
│   └── vector_store.py
│
├── data
│   └── clean_restaurants_dataset.csv
│
├── app.py
├── test_llm.py
├── test_rag.py
└── README.md
```

---

# ▶️ How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# 🚀 Future Improvements

- Add more restaurant data sources.
- Improve recommendation ranking.
- Add additional AI models.
- Deploy on Streamlit Community Cloud.
- Add user feedback learning.

---

# 👩‍💻 Author

**Mandulee Laknara**
