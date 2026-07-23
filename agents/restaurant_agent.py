from rag.vector_store import RestaurantRAG
from agents.llm_agent import LLMAgent


class RestaurantAgent:


    def __init__(self):

        self.rag = RestaurantRAG()

        self.llm = LLMAgent()



    def get_recommendation(
        self,
        user_query
    ):

        # Step 1: Retrieve relevant restaurants
        retrieved_documents = self.rag.search(
            user_query,
            k=3
        )


        # Step 2: Generate AI response
        response = self.llm.generate_response(
            user_query,
            retrieved_documents
        )


        return response