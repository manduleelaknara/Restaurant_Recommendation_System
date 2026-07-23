from rag.vector_store import RestaurantRAG
from agents.llm_agent import LLMAgent
from agents.review_agent import ReviewAgent


class RestaurantAgent:


    def __init__(self):

        self.rag = RestaurantRAG()

        self.review_agent = ReviewAgent()

        self.llm = LLMAgent()



    def get_recommendation(
        self,
        user_query
    ):


        # Agent 1: Restaurant Agent retrieves restaurants
        retrieved_documents = self.rag.search(
            user_query,
            k=5
        )


        # Agent 2: Review Agent analyzes retrieved results
        reviewed_documents = self.review_agent.analyze_reviews(
            retrieved_documents
        )


        # LLM generates final response
        response = self.llm.generate_response(
            user_query,
            reviewed_documents
        )


        return response