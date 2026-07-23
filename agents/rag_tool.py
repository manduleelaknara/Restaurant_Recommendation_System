from rag.vector_store import RestaurantRAG


class RestaurantSearchTool:


    def __init__(self):

        self.rag = RestaurantRAG()



    def search_restaurants(
        self,
        query
    ):

        """
        RAG retrieval tool used by Restaurant Agent
        """

        results = self.rag.search(
            query,
            k=5
        )

        return results