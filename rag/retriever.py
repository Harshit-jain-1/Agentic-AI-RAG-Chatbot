{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdaf9581-a358-4e65-92d1-c55ed5ba7fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain.text_splitter import RecursiveCharacterTextSplitter\n",
    "\n",
    "def chunk_text(text):\n",
    "    splitter = RecursiveCharacterTextSplitter(\n",
    "        chunk_size=800,\n",
    "        chunk_overlap=150\n",
    "    )\n",
    "    return splitter.split_text(text)"
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
