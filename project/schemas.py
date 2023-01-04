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
        

# Character schema
class CharacterBase(BaseModel):
    name: str

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int

    class Config:
        orm_mode = True


# Admin schema
class AdminBase(BaseModel):
    username: str

class AdminCreate(AdminBase):
    password: str

class Admin(AdminBase):
    id: int

    class Config:
        orm_mode = True
