from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Sadi!"}

@app.get("/hello/{name}")
def greet(name: str, age: int = 21):
    return {"greeting": f"Hi {name}", "age": age}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return {"you_sent": item}


todos = [] 
new_id = 1 

class TodoCreate (BaseModel) :
    tittle : str 
    done : bool = False 
    

@app.post ("/todos")
def add_todo (todo : TodoCreate) :
    global next_id 
    new_todo = {"id" : new_id, "tittel" : todo.tittle, "done" : todo.done}
    todos.append (new_todo)
    new_id += 1 
    return new_todo 





