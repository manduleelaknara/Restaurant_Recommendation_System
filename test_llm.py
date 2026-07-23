from rag.vector_store import RestaurantRAG
from agents.llm_agent import LLMAgent


rag = RestaurantRAG()
llm = LLMAgent()

query = "Recommend seafood restaurants in Colombo."

documents = rag.search(query)

response = llm.generate_response(
    query,
    documents
)

print(response)