from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tag: list = []

@app.put('items/{item_id}')
async def update_item(
    item_id: int, item: Item
):
    results = {"item_id": item_id, "item": item}
    return results