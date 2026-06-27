from fastapi import FastAPI,Depends
from database import get_db,engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app=FastAPI()

class BookSchema(BaseModel):
    id:int
    title:str
    author:str
    published_year:int


@app.post("/books")
def create_book(book:BookSchema,db:Session=Depends(get_db)):
    db_book=model.Book(id=book.id,title=book.title,author=book.author,published_year=book.published_year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book 

@app.get("/books")
def get_books(db:Session=Depends(get_db)):
    books=db.query(model.Book).all()
    return books

@app.get("/books/{book_id}")
def get_book(book_id:int,db:Session=Depends(get_db)):
    book=db.query(model.Book).filter(model.Book.id==book_id).first()
    if not book:
        return {"message":"Book not found"}
    return book
