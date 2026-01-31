{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdaf9581-a358-4e65-92d1-c55ed5ba7fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_openai import ChatOpenAI\n",
    "from config import *\n",
    "\n",
    "llm = ChatOpenAI(\n",
    "    model=LLM_MODEL,\n",
    "    temperature=0,\n",
    "    openai_api_key=OPENAI_API_KEY\n",
    ")\n",
    "\n",
    "SYSTEM_PROMPT = \"\"\"\n",
    "You are an AI assistant.\n",
    "Answer ONLY using the provided context.\n",
    "If the answer is not present, say:\n",
    "\"I don't know based on the provided document.\"\n",
    "\"\"\"\n",
    "\n",
    "def generate_answer(question, contexts):\n",
    "    context_text = \"\\n\\n\".join(contexts)\n",
    "\n",
    "    messages = [\n",
    "        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n",
    "        {\"role\": \"user\", \"content\": f\"Context:\\n{context_text}\\n\\nQuestion:\\n{question}\"}\n",
    "    ]\n",
    "\n",
    "    response = llm.invoke(messages)\n",
    "    return response.content\n"
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
