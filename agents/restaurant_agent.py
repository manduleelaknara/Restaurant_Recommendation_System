from agents.rag_tool import RestaurantSearchTool
from agents.llm_agent import LLMAgent
from agents.review_agent import ReviewAgent
from agents.reflection_agent import ReflectionAgent


class RestaurantAgent:

    """
    Orchestrator Agent

    Handles communication between:
    User Agent
    RAG Tool
    Review Agent
    LLM Agent
    Reflection Agent
    """


    def __init__(self):

        # Tool-use Pattern
        self.search_tool = RestaurantSearchTool()

        # Worker Agents
        self.review_agent = ReviewAgent()

        self.llm = LLMAgent()

        # Reflection Pattern
        self.reflection_agent = ReflectionAgent()



    def receive_user_request(
        self,
        user_message
    ):

        """
        Receives structured message from UserAgent
        """

        user_query = str(
            user_message["data"]["query"]
        )

        return self.get_recommendation(
            user_query
        )



    def send_to_review_agent(
        self,
        restaurants
    ):

        """
        Structured message sent to Review Agent
        """

        review_message = {

            "sender": "RestaurantAgent",

            "receiver": "ReviewAgent",

            "message_type": "restaurant_analysis",

            "data": restaurants

        }


        ranked_results = self.review_agent.analyze_reviews(
            review_message["data"]
        )


        return ranked_results



    def get_recommendation(
        self,
        user_query
    ):


        # -------------------------------
        # Step 1:
        # RAG Tool Communication
        # -------------------------------

        retrieved_documents = self.search_tool.search_restaurants(
            user_query
        )


        # -------------------------------
        # Step 2:
        # RestaurantAgent -> ReviewAgent
        # -------------------------------

        ranked_documents = self.send_to_review_agent(
            retrieved_documents
        )


        # -------------------------------
        # Step 3:
        # LLM Agent Response Generation
        # -------------------------------

        response = self.llm.generate_response(
            user_query,
            ranked_documents
        )


        # -------------------------------
        # Step 4:
        # Reflection Agent Validation
        # -------------------------------

        final_response = self.reflection_agent.review_response(
            response,
            ranked_documents
        )


        return final_response