from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

app = FastAPI()

todos = [] 
new_id = 1 

class TodoCreate (BaseModel) :
    title : str 
    done : bool = False 
    
    
@app.get("/", response_class=PlainTextResponse)
def home():
    lines = []
    lines = ["My Todo List For Today :", ""]
    for todo in todos:
        if todo["done"]:
            mark = "✅"
        else:
            mark = "⬜"
        lines.append(f"{todo['id']}. {todo['title']} {mark}")
    return "\n".join(lines)

@app.post ("/todos")
def add_todo (todo : TodoCreate) :
    global new_id 
    new_todo = {"id" : new_id, "title" : todo.title, "done" : todo.done}
    todos.append (new_todo)
    new_id += 1 
    return new_todo 


@app.get("/todos")
def list_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}")
def mark_done(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Task Done"}
    raise HTTPException(status_code=404, detail="Todo not found")




