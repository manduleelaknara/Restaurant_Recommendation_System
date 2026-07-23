import pandas as pd
import os


def create_documents():

    file_path = os.path.join(
        "data",
        "clean_restaurants_dataset.csv"
    )

    df = pd.read_csv(file_path)

    documents = []

    for _, row in df.iterrows():

        text = f"""
        Restaurant: {row['Restaurant_Name']}
        Cuisine: {row['Cuisine']}
        Location: {row['Location']}
        Budget: {row['Budget']}
        Rating: {row['Rating']}
        Review: {row['Review']}
        """

        documents.append(text)

    return documents