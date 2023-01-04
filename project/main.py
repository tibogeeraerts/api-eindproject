#main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os
import random

import crud, models, schemas, auth
from database import SessionLocal, engine

# make database dir if it doesn't exist
if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# create tables in database 'database.db' (check datapase.py database-URL)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# make database session/connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# allowed origins for CORS
origins = ["*"]

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    admin = auth.authenticate_admin(db, form_data.username, form_data.password)
    if not admin:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": admin.username}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

# populate database with quotes on startup
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    if len(db.query(models.Quote).all()) == 0:
        print(crud.populate_database(db))
    else:
        print("INFO:     Database already populated!")

# POST custom quote
@app.post("/quotes/", response_model=schemas.Quote)
async def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    new_quote = crud.create_quote(db=db, quote=quote)
    return new_quote

# GET all quotes
@app.get("/quotes/all", response_model=list[schemas.Quote])
async def read_quotes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db, skip=skip, limit=limit)
    return quotes

# GET random quote
@app.get("/quotes/random", response_model=schemas.Quote)
async def read_quote_random(db: Session = Depends(get_db)):
    quotes = crud.get_quotes(db)
    quote = random.choice(quotes)
    return quote

# GET last quote
@app.get("/quotes/last", response_model=schemas.Quote)
async def read_quote_last(db: Session = Depends(get_db)):
    quote = crud.get_quote_last(db)
    return quote

# PUT last quote
@app.put("/quotes/last", response_model=schemas.Quote)
async def update_quote_last(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    updated_quote = crud.update_quote_last(db, quote)
    return updated_quote

# DELETE last quote
@app.delete("/quotes/last", response_model=schemas.Quote)
async def delete_quote_last(db: Session = Depends(get_db)):
    deleted_quote = crud.delete_quote_last(db)
    return deleted_quote

# create admin
@app.post("/admin/", response_model=schemas.Admin)
async def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    new_admin = crud.create_admin(db=db, admin=admin)
    return new_admin

# GET current admin
@app.get("/admin/me", response_model=schemas.Admin)
def read_admin_me(db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    current_admin = auth.get_current_admin(db, token)
    return current_admin