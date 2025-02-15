from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI()

documents = [
    {
        "id": 0,
        "text": """
        É um conceito muito estudado  na psicologia, que diz que se uma pessoa já fez algo que considera bom ou positivo, ela tem uma probabilidade menor de fazer algo positivo logo a seguir

        EX : "Você enquanto anda na rua dá dois reais a um mendigo, se outro mendigo de abordar posteriormente, você tem uma probabilidade menor de dar dois reais a esse segundo mendigo
        """
    },
    {
        "id": 1,
        "text": """
            Competitividade é uma variável que incorpora fatores, geralmente associados com o desejo de excelência, em comparação com outros, pelo prazer de competir
        """
    },
    {
        "id": 2,
        "text": """
            A liquidez das relações, também diz respeito a destruição de protocolos sociais relacionados a criação de laços sociais

            Como no caso do mundo contemporâneo, onde os protocolos de frequência e presença foram modificados, de modo que diferente de uma rede social, em uma interação presencial você tem mais dificuldade em se "Desconectar
        """
    }
]

model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embeddings = { doc["id"] : model.encode(doc["text"],convert_to_tensor=True) for doc in documents}

class QueryRequest(BaseModel):
    query:str


@app.post("/query")
def query_rag(request:QueryRequest):
    query_embeding = model.encode(request.query, convert_to_tensor=True)
    best_doc = {}
    best_score = float("-inf")

    for doc in documents:
        score = util.cos_sim(query_embeding, doc_embeddings[doc["id"]])
        if score > best_score:
            best_score = score
            best_doc = doc
    # obtem o documento mais próximos
    doc = {"document": best_doc.get("text")}
    return doc