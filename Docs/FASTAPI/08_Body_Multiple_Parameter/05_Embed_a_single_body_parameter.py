from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

"""
In this case FastAPI will expect a body like:
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}

instead of:
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
"""
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put('items/{item_id}')
async def update_item(
    item_id: int, item: Annotated[Item, Body(embed=True)]
):
    results = {"item_id": item_id, "item": item}
    return results
