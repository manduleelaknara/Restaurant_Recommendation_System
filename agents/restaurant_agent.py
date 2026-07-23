from agents.rag_tool import RestaurantSearchTool
from agents.llm_agent import LLMAgent
from agents.review_agent import ReviewAgent
from agents.reflection_agent import ReflectionAgent


class RestaurantAgent:

    """
    Orchestrator Agent

    This agent controls the complete workflow:
    1. Uses RAG Search Tool to retrieve restaurants
    2. Sends retrieved information to Review Agent
    3. Sends ranked results to LLM Agent
    4. Reflects and validates final response
    5. Returns final recommendation
    """


    def __init__(self):

        # Tool-use Pattern
        self.search_tool = RestaurantSearchTool()

        # Worker Agents
        self.review_agent = ReviewAgent()

        self.llm = LLMAgent()

        # Reflection Pattern
        self.reflection_agent = ReflectionAgent()



    def get_recommendation(
        self,
        user_query
    ):


        # Step 1:
        # Retrieve restaurant information using tool

        retrieved_documents = self.search_tool.search_restaurants(
            user_query
        )


        # Step 2:
        # Analyze and rank restaurants

        ranked_documents = self.review_agent.analyze_reviews(
            retrieved_documents
        )


        # Step 3:
        # Generate AI response

        response = self.llm.generate_response(
            user_query,
            ranked_documents
        )


        # Step 4:
        # Reflection Agent validates response

        final_response = self.reflection_agent.review_response(
            response,
            ranked_documents
        )


        # Step 5:
        # Return improved response

        return final_response