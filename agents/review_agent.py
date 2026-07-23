class ReviewAgent:


    def analyze_reviews(self, restaurants):

        if not restaurants:
            return restaurants


        scored_restaurants = []


        for restaurant in restaurants:

            score = 0


            if "Rating:" in restaurant:

                try:
                    rating = restaurant.split("Rating:")[1].split("\n")[0].strip()
                    score = float(rating) * 20

                except:
                    score = 0


            scored_restaurants.append(
                {
                    "information": restaurant,
                    "score": score
                }
            )


        scored_restaurants = sorted(
            scored_restaurants,
            key=lambda x: x["score"],
            reverse=True
        )


        return [
            item["information"]
            for item in scored_restaurants
        ]