from pydantic import BaseModel

class Book(BaseModel):
    id : int
    title: str
    author: str
    page_num: int
    review: str