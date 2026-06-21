from  fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from typing import Optional
books=[
    {
        "id":1,
        "title":"The Great Gatsby",
        "author":"F. Scott Fitzgerald",
        "published_year":1925
    },
    {
        "id":2,
        "title":"To Kill a Mockingbird",
        "author":"Harper Lee",
        "published_year":1960
        },
        {
            "id":3,
            "title":"1984",
            "author":"George Orwell",
            "published_year":1948
        },
        {
            "id":4,
            "title":"Pride and Prejudice",
            "author":"Jane Austen",
            "published_year":1813
        },
        {
            "id":5,
            "title":"The Catcher in the Rye",
            "author":"J.D. Salinger",
            "published_year":1951
        }

]

app=FastAPI()
@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")


class Book(BaseModel):
    id:int
    title:str
    author:str
    published_year:int

@app.post("/books")
def create_book(book:Book):
    books.append(book.dict())
    return book

class BookUpdate(BaseModel):
    title:str
    author:str
    published_year:int

@app.put("/books/{book_id}")
def update_book(book_id:int,book_update:BookUpdate):
    for book in books:
        if book['id']==book_id:
            book['title']=book_update.title
            book['author']=book_update.author
            book['published_year']=book_update.published_year
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

class UserUpdate(BaseModel):
    title:Optional[str]=None
    author:Optional[str]=None
    published_year:Optional[int]=None

@app.patch("/books/{book_id}")
def Userupdate(book_id:int,book_update:UserUpdate):
    update_book=book_update.model_dump(exclude_unset=True)
    for book in books:
        if book["id"] == book_id:

            for key, value in update_book.items():
                book[key] = value

            return book


@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return {"messsage":"Book has been deleted successfully!"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")