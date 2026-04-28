from rag.vector_db import search_docs

def retrieve_answer(query):
    results = search_docs(query)
    return f"Knowledge Base Answer: {results}"
