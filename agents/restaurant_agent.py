from agents.rag_tool import RestaurantSearchTool
from agents.llm_agent import LLMAgent
from agents.review_agent import ReviewAgent


class RestaurantAgent:

    """
    Orchestrator Agent

    This agent controls the complete workflow:
    1. Uses RAG Search Tool to retrieve restaurants
    2. Sends retrieved information to Review Agent
    3. Sends ranked results to LLM Agent
    4. Returns final recommendation
    """


    def __init__(self):

        # Tool-use Pattern
        self.search_tool = RestaurantSearchTool()

        # Worker Agents
        self.review_agent = ReviewAgent()

        self.llm = LLMAgent()



    def get_recommendation(
        self,
        user_query
    ):


        # ---------------------------------
        # Step 1:
        # Use RAG Search Tool
        # ---------------------------------

        retrieved_documents = self.search_tool.search_restaurants(
            user_query
        )


        # ---------------------------------
        # Step 2:
        # Review Agent Ranking
        # ---------------------------------

        ranked_documents = self.review_agent.analyze_reviews(
            retrieved_documents
        )


        # ---------------------------------
        # Step 3:
        # LLM Agent Response Generation
        # ---------------------------------

        response = self.llm.generate_response(
            user_query,
            ranked_documents
        )


        # ---------------------------------
        # Step 4:
        # Return Final Recommendation
        # ---------------------------------

        return response