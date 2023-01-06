#crud.py
import requests
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import auth
import models
import schemas


# get quote from external API
def call_api(url: str):
    response = requests.get(url)
    return response.json()['data']['content']

# populate database with quotes from API
def populate_database(db: Session):
    for i in range(0, 20):
        quote = call_api('https://officeapi.dev/api/quotes/random')
        db_quote = models.Quote(content=quote)
        db.add(db_quote)
        db.commit()
        db.refresh(db_quote)
    return "INFO:     Database populated!"

# make new quote
def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(content=quote.content)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

# get quote by id
def get_quote(db: Session, quote_id: int):
    quote_by_id = db.query(models.Quote).filter(models.Quote.id == quote_id).first()
    return quote_by_id

# get all quotes (max 50)
def get_quotes(db: Session, skip: int = 0, limit: int = 50):
    all_quotes = db.query(models.Quote).offset(skip).limit(limit).all()
    return all_quotes

# get last quote in database
def get_quote_last(db: Session):
    db_quote = db.query(models.Quote).all()
    quote = db_quote[-1]
    return quote

# update last quote in database
def update_quote_last(db: Session, updated_quote: schemas.QuoteCreate):
    db_quote = db.query(models.Quote).all()
    quote = db_quote[-1]
    quote.content = updated_quote.content
    db.commit()
    return quote

# delete last quote in database
def delete_quote_last(db: Session):
    db_quote = db.query(models.Quote).all()
    quote = db_quote[-1]
    db.delete(quote)
    db.commit()
    return quote

# create admin
def create_admin(db: Session, admin: schemas.AdminCreate):
    hashed_password = auth.get_password_hash(admin.password)
    db_admin = models.Admin(username=admin.username, hashed_password=hashed_password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

# get admin by username
def get_admin_username(db: Session, username: str):
    admin = db.query(models.Admin).filter(models.Admin.username == username).first()
    return admin

# delete admin by username
def delete_admin(db: Session, admin: schemas.Admin):
    admin = db.query(models.Admin).filter(models.Admin.username == admin.username).first()
    db.delete(admin)
    db.commit()
    return admin

# create character (only for admin)
def create_character(db: Session, character: schemas.CharacterCreate):
    db_character = models.Character(name=character.name)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

# get all characters
def get_all_characters(db: Session):
    all_characters = db.query(models.Character).all()
    return all_characters