class UserAgent:

    def get_preferences(
        self,
        location,
        cuisine,
        budget,
        rating
    ):

        preferences = {
            "location": location,
            "cuisine": cuisine,
            "budget": budget,
            "rating": rating
        }

        return preferences