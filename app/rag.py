import os
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from utils import extract_text_from_pdf, extract_text_from_textfile

COLLECTION_NAME = "user_study_materials"
chroma_client = chromadb.Client(Settings())
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def get_collection():
    return chroma_client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

def add_user_document(user_id, file_path):
    collection = get_collection()
    text = ""
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".txt"):
        text = extract_text_from_textfile(file_path)
    else:
        raise ValueError("Unsupported file format. Upload PDF or TXT files only.")

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    collection.add(
        documents=chunks,
        metadatas=[{"user_id": str(user_id), "source": file_path}] * len(chunks),
        ids=[f"{user_id}_{file_path}_{i}" for i in range(len(chunks))]
    )

def search_similar(user_id, query, top_k=5):
    collection = get_collection()
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        where={"user_id": str(user_id)}
    )
    return results.get("documents", [[]])[0]
