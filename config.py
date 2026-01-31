{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdaf9581-a358-4e65-92d1-c55ed5ba7fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "\n",
    "load_dotenv()\n",
    "\n",
    "OPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\")\n",
    "PINECONE_API_KEY = os.getenv(\"PINECONE_API_KEY\")\n",
    "PINECONE_ENV = os.getenv(\"PINECONE_ENVIRONMENT\")\n",
    "PINECONE_INDEX = os.getenv(\"PINECONE_INDEX\")\n",
    "\n",
    "EMBEDDING_MODEL = \"text-embedding-3-small\"\n",
    "LLM_MODEL = \"gpt-4o-mini\"\n"
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
