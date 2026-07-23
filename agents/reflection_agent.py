import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class ReflectionAgent:


    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )


        # Model used for reflection and evaluation
        self.model = "llama-3.3-70b-versatile"



    def review_response(
        self,
        response,
        retrieved_documents
    ):

        """
        Reflection Pattern:

        Evaluates the generated recommendation
        and improves the response if required.
        """


        if not response:

            return "No recommendation available."



        context = "\n".join(
            retrieved_documents
        )



        prompt = f"""
You are a Reflection Agent for a Restaurant Recommendation AI system.

Your responsibility:
1. Check whether the recommendation is based only on the given restaurant information.
2. Ensure no fake restaurant names are generated.
3. Ensure the answer is clear and useful for the user.
4. Improve the answer if necessary.

If the answer is already correct, return it without changes.

Restaurant Information:

{context}


Generated Recommendation:

{response}


Return only the final improved recommendation.
"""



        result = self.client.chat.completions.create(

            model=self.model,

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.1
        )



        return result.choices[0].message.content