from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    types: list[str]