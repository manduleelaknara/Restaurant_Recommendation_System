import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from rag.create_documents import create_documents


class RestaurantRAG:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.documents = create_documents()

        embeddings = self.model.encode(
            self.documents
        )

        self.embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        self.index = faiss.IndexFlatL2(
            self.embeddings.shape[1]
        )

        self.index.add(
            self.embeddings
        )

    def search(self, query, k=3):

        query_embedding = self.model.encode(
            [query]
        )

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for i in indices[0]:
            results.append(
                self.documents[i]
            )

        return results