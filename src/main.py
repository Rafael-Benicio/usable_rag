from fastapi import FastAPI
from pydantic import BaseModel
from src.rag_content import load_raw_content
from sentence_transformers import SentenceTransformer, util

app = FastAPI()


documents = load_raw_content()

model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embeddings = {doc["id"]: model.encode(
    doc["text"], convert_to_tensor=True) for doc in documents}


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_rag(request: QueryRequest):
    query_embeding = model.encode(request.query, convert_to_tensor=True)
    best_doc = {}
    best_score = float("-inf")

    for doc in documents:
        score = util.cos_sim(query_embeding, doc_embeddings[doc["id"]])
        if score > best_score:
            best_score = score
            best_doc = doc
    doc = {"document": best_doc.get("text")}

    return doc
