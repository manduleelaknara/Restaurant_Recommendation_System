import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class LLMAgent:


    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )


        # Model used for recommendation generation
        self.model = "llama-3.1-8b-instant"



    def generate_response(
        self,
        user_query,
        retrieved_documents
    ):


        context = "\n".join(
            retrieved_documents
        )


        prompt = f"""
You are an AI Restaurant Recommendation Assistant.

IMPORTANT RULES:

1. Recommend ONLY restaurants from the provided information.
2. Never create restaurant names.
3. Explain recommendations using rating, cuisine, budget and reviews.

User Query:
{user_query}


Restaurant Information:
{context}


Provide a clear recommendation summary.
"""



        response = self.client.chat.completions.create(

            model=self.model,

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.2
        )


        return response.choices[0].message.content