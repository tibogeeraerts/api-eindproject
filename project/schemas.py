# schemas.py

from pydantic import BaseModel

# Quote schema
class QuoteBase(BaseModel):
    content: str


class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int

    class Config:
        orm_mode = True
        