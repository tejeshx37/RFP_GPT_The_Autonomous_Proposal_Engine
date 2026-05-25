# Shadow Strikers RFP Demo

Autonomous discovery, analysis, and proposal generation for B2B tenders.

## Overview
This is a Streamlit-based web application that automates the Request for Proposal (RFP) response process using a multi-agent AI framework (powered by CrewAI and Google Gemini). It allows users to upload an RFP PDF, which is then processed by a crew of specialized AI agents to extract requirements, find the best matching SKU from a catalog, calculate pricing, and draft a professional proposal.

## Features
- **PDF Processing**: Upload and extract text from RFP documents.
- **Multi-Agent Architecture**:
  - **Technical Matching Engineer**: Maps RFP requirements to the best-matching SKUs using local HuggingFace embeddings and FAISS for vector search.
  - **Pricing Strategist**: Computes margin-safe competitive prices based on the selected SKU's cost.
  - **Proposal Orchestrator**: Generates a structured, professional proposal draft formatted in Markdown.
- **Vector Search Catalog**: Uses FAISS and `all-MiniLM-L6-v2` for fast and free local vector embeddings to search the product catalog (`data/catalog.csv`).
- **Google Gemini Integration**: Uses `gemini-flash-latest` via LangChain for fast, intelligent agent behavior.
- **Graceful Degradation**: Built-in fallback mock data to ensure demo continuity in case of API rate limits or failures.

## Installation
1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a `.env` file in the root directory and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage
Run the Streamlit application:
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501` to use the application.

## Technologies Used
- Streamlit
- CrewAI
- LangChain & Google Generative AI (Gemini)
- HuggingFace Embeddings
- FAISS (Vector Store)
- PyPDF & Pandas
