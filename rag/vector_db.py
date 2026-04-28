from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()

collection = client.create_collection("kb")

docs = [
    "To reset password, go to settings.",
    "Install software from company portal.",
    "Check network cables if internet not working."
]

for i, doc in enumerate(docs):
    collection.add(documents=[doc], ids=[str(i)])

def search_docs(query):
    result = collection.query(query_texts=[query], n_results=1)
    return result['documents'][0][0]
