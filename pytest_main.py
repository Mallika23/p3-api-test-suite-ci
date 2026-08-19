from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List,Optional

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

#Mock database
todo_items = {}

@app.get("/todos", response_model=List[TodoItem])
async def read_todos():
    return list(todo_items.values())

@app.post("/todos", response_model=TodoItem)
async def create_todo(item: TodoItem):
    todo_id = str(len(todo_items) + 1)
    #item.id = int(todo_id)
    todo_items[todo_id] = item
    return item

@app.get("/todos/{todo_id}", response_model=TodoItem)
async def read_todo(todo_id: int):
    item = todo_items.get(str(todo_id))
    if item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return item

@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: int, item: TodoItem):
    if str(todo_id) not in todo_items:
        raise HTTPException(status_code=404, detail="Todo item not found")
    todo_items[str(todo_id)] = item
    return item

@app.delete("/todos/{todo_id}", response_model=TodoItem)
async def delete_todo(todo_id: int):
    item = todo_items.pop(str(todo_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return item