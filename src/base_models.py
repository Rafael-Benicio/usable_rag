from pydantic import BaseModel


class RawContent(BaseModel):
    id: int
    text: str


class QueryRequest(BaseModel):
    query: str

