import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()
model = SentenceTransformer(os.getenv("EMBEDDING_MODEL"))

def get_embeddings(text_chunks):
    return model.encode(text_chunks)

def create_faiss_index(embeddings):
    embeddings = np.array(embeddings)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_similar_chunks(query, text_chunks, index):
    query_vector = model.encode([query])
    scores, indices = index.search(np.array(query_vector), k=3)
    return [text_chunks[i] for i in indices[0]]



