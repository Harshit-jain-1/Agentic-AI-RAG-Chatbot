{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdaf9581-a358-4e65-92d1-c55ed5ba7fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pypdf import PdfReader\n",
    "from langchain_openai import OpenAIEmbeddings\n",
    "from pinecone import Pinecone\n",
    "from config import *\n",
    "from ingest.chunking import chunk_text\n",
    "import uuid\n",
    "\n",
    "def ingest_pdf(pdf_path):\n",
    "    reader = PdfReader(pdf_path)\n",
    "    full_text = \"\"\n",
    "\n",
    "    for page in reader.pages:\n",
    "        full_text += page.extract_text()\n",
    "\n",
    "    chunks = chunk_text(full_text)\n",
    "\n",
    "    embeddings = OpenAIEmbeddings(\n",
    "        model=EMBEDDING_MODEL,\n",
    "        openai_api_key=OPENAI_API_KEY\n",
    "    )\n",
    "\n",
    "    pc = Pinecone(api_key=PINECONE_API_KEY)\n",
    "    index = pc.Index(PINECONE_INDEX)\n",
    "\n",
    "    vectors = []\n",
    "    for chunk in chunks:\n",
    "        vector = embeddings.embed_query(chunk)\n",
    "        vectors.append({\n",
    "            \"id\": str(uuid.uuid4()),\n",
    "            \"values\": vector,\n",
    "            \"metadata\": {\"text\": chunk}\n",
    "        })\n",
    "\n",
    "    index.upsert(vectors)\n",
    "    print(f\"Ingested {len(vectors)} chunks.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    ingest_pdf(\"data/Ebook-Agentic-AI.pdf\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
