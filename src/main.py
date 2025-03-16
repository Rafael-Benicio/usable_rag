from fastapi import FastAPI
from sentence_transformers import SentenceTransformer, util
from src.rag_content import load_raw_content
from src.base_models import QueryRequest
from src.embedding import load_embeddings

app = FastAPI()

documents = load_raw_content('./My')

model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embeddings = load_embeddings(model, documents)

print("================   RUNNING   ==================")

@app.post("/query")
def query_rag(request: QueryRequest):
    query_embeding = model.encode(request.query, convert_to_tensor=True)
    best_doc = {}
    best_score = float("-inf")

    for doc in documents:
        score = util.cos_sim(query_embeding, doc_embeddings[doc.id])
        if score > best_score:
            best_score = score
            best_doc = doc
    doc = best_doc

    return doc
