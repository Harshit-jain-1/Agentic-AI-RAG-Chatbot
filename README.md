# Agentic AI RAG Chatbot

RAG-based AI chatbot built using LangGraph, Pinecone, and OpenAI.

## Setup

1. Clone repository
2. Create `.env`
3. Install dependencies:
   pip install -r requirements.txt

4. Create Pinecone index (dimension 1536)
5. Ingest PDF:
   python ingest/ingest_pdf.py

6. Run API:
   uvicorn api.app:app --reload

## Endpoint

POST /chat
{
  "question": "What is Agentic AI?"
}

## Response
- Answer
- Retrieved Context
- Confidence Score
