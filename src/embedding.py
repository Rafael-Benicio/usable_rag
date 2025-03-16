from os import path
import pickle
from typing import List

from sentence_transformers import SentenceTransformer

from src.base_models import RawContent

EMBEDDINGS_FILE = 'embeddings.npy'


def load_embeddings(model: SentenceTransformer, documents: List[RawContent]) -> dict:
    doc_embeddings = None
    if path.isfile(EMBEDDINGS_FILE):
        with open(EMBEDDINGS_FILE, "rb") as bin_data:
            doc_embeddings = pickle.load(bin_data)
            print("================ DATA-LOADED ==================")
    else:
        doc_embeddings = {doc.id: model.encode(
            doc.text, convert_to_tensor=True) for doc in documents}

        with open(EMBEDDINGS_FILE, "wb") as bin_data:
            pickle.dump(doc_embeddings, bin_data)
    return doc_embeddings
