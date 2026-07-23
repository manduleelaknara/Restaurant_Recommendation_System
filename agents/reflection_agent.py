class ReflectionAgent:


    def review_response(
        self,
        response,
        retrieved_documents
    ):

        """
        Reflection Pattern:
        Checks generated response quality
        and improves if required.
        """


        if not response:

            return "No recommendation available."


        # Check whether response contains
        # restaurant information

        has_restaurant_info = False


        for document in retrieved_documents:

            if document.lower() in response.lower():

                has_restaurant_info = True
                break



        if has_restaurant_info:

            return response


        else:

            return (
                response
                +
                "\n\nNote: Recommendation generated "
                "based on available restaurant information."
            )