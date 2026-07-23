class ReviewAgent:

    def analyze_reviews(self, restaurants):

        if len(restaurants) == 0:
            return restaurants

        restaurants = restaurants.copy()

        restaurants["Recommendation_Score"] = (
            restaurants["Rating"] * 20
        )

        return restaurants.sort_values(
            by="Recommendation_Score",
            ascending=False
        )