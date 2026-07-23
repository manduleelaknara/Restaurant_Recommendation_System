class UserAgent:


    def create_request(
        self,
        location,
        cuisine,
        budget,
        rating
    ):

        """
        Creates a structured message
        to communicate with Restaurant Agent.
        """


        message = {

            "sender": "UserAgent",

            "receiver": "RestaurantAgent",

            "message_type": "restaurant_request",

            "data": {

                "location": location,

                "cuisine": cuisine,

                "budget": budget,

                "rating": rating

            }

        }


        return message