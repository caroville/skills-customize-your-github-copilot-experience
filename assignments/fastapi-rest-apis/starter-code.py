# Starter Code: FastAPI REST API

from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items = [
    {
        "id": 1,
        "name": "Keyboard",
        "description": "Wireless mechanical keyboard",
        "price": 49.99,
        "in_stock": True,
    },
    {
        "id": 2,
        "name": "Mouse",
        "description": "Wireless mouse",
        "price": 29.99,
        "in_stock": True,
    },
    {
        "id": 3,
        "name": "Monitor",
        "description": "24-inch HD monitor",
        "price": 149.99,
        "in_stock": False,
    },
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Shop API"}

@app.get("/items")
def list_items(q: Optional[str] = None, available: Optional[bool] = None) -> List[Item]:
    results = [Item(**item) for item in items]
    if q:
        results = [item for item in results if q.lower() in item.name.lower() or (item.description and q.lower() in item.description.lower())]
    if available is not None:
        results = [item for item in results if item.in_stock == available]
    return results

@app.get("/items/{item_id}")
def read_item(item_id: int) -> Item:
    for item in items:
        if item["id"] == item_id:
            return Item(**item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: Item) -> Item:
    if any(existing_item["id"] == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item.dict())
    return item

# Run the app with:
# uvicorn starter-code:app --reload
# Then visit http://127.0.0.1:8000/docs to see the automatic API documentation.
