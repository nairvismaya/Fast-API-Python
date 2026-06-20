from fastapi import FastAPI
from typing import Optional
app=FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello, World!"}

@app.get("/greet")
def greet():
    return {"Message":"Welcome to FastAPI!"}

@app.get("/greet/{name}")
def greet_name(name:str,age:Optional[int]=None):
    return {"Message":f"Hello, {name} and you are {age} years old!"}