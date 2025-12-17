import pandas as pd
import faiss
import numpy as np
import os
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

def build_catalog_index(csv_path="data/catalog.csv"):
    """
    Load catalog CSV, generate embeddings, and build FAISS index.
    Returns (index, dataframe).
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Catalog file not found at {csv_path}")

    df = pd.read_csv(csv_path)
    
    # Use Local HuggingFace Embeddings (free, no API key needed, robust)
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    descriptions = df['description'].tolist()
    
    # Embed documents
    embeddings = embeddings_model.embed_documents(descriptions)
    embeddings_np = np.array(embeddings).astype('float32')
    
    # Build FAISS index
    dimension = embeddings_np.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_np)
    
    return index, df

def search_best_sku(requirement_text, index, dataframe, top_k=3):
    """
    Search best SKU matching the requirement text.
    Returns top-k SKUs from dataframe with scores.
    """
    # Use same model for query
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Embed query
    query_embedding = embeddings_model.embed_query(requirement_text)
    query_np = np.array([query_embedding]).astype('float32')
    
    # Search
    distances, indices = index.search(query_np, top_k)
    
    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(dataframe):
            item = dataframe.iloc[idx].to_dict()
            item['score'] = float(distances[0][i]) 
            results.append(item)
            
    return results
