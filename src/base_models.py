from pydantic import BaseModel


class RawContent(BaseModel):
    id: int
    title: str
    text: str


class QueryRequest(BaseModel):
    query: str
