from rag.vector_store import RestaurantRAG


rag = RestaurantRAG()

results = rag.search(
    "Best seafood restaurants in Colombo"
)

for r in results:
    print(r)