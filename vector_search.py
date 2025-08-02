import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()
embedding_model_name = os.getenv("EMBEDDING_MODEL")

if not embedding_model_name:
    raise ValueError("EMBEDDING_MODEL not found in .env file")

model = SentenceTransformer(embedding_model_name)

def get_embeddings(text_chunks):
    return model.encode(text_chunks, convert_to_numpy=True)

def create_faiss_index(embeddings):
    embeddings = np.array(embeddings).astype('float32')
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_similar_chunks(query, text_chunks, index, top_k=3):
    query_vector = model.encode([query], convert_to_numpy=True).astype('float32')
    scores, indices = index.search(query_vector, k=top_k)
    return [text_chunks[i] for i in indices[0]]
