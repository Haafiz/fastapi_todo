from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_welcome():
    return {"detail": "Welcome to To Do items, try /todo_items CRUD"}


@app.get("/todo_items", response_model=List[schemas.TodoItemResponse])
def get_all_todo_items(db: Session = Depends(get_db)):
    todo_items = db.query(models.TodoItem).all()
    return todo_items


@app.get("/todo_items/{item_id}", response_model=schemas.TodoItemResponse)
def get_todo_item(item_id: int, response: Response, db: Session = Depends(get_db)):
    todo_item = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if not todo_item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="This todo item doesn't exist")

    return todo_item


@app.post("/todo_items", status_code=status.HTTP_201_CREATED, response_model=schemas.TodoItemResponse)
def create_todo_item(request: schemas.TodoItem, db: Session = Depends(get_db)):
    new_todo_item = models.TodoItem(title=request.title, description=request.description)
    db.add(new_todo_item)
    db.commit()
    db.refresh(new_todo_item)

    return new_todo_item


@app.put("/todo_items/{item_id}", response_model=schemas.TodoItemResponse)
def update_todo_item(item_id: int, request: schemas.TodoItem, db: Session = Depends(get_db)):
    todo_item = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if not todo_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This todo item doesn't exist")
    todo_item.update({'title': request.title, 'description': request.description}, synchronize_session=False)
    db.commit()
    db.refresh(todo_item)

    return todo_item


@app.delete("/todo_items/{item_id}")
def delete_todo_item(item_id: int,  db: Session = Depends(get_db)):
    todo_item = db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()
    if not todo_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This todo item doesn't exist")
    todo_item.delete(synchronize_session=False)
    db.commit()

    return {"deleted": item_id}