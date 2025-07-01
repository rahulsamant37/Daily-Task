from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

"""
When using any of:

Path()
Query()
Header()
Cookie()
Body()
Form()
File()
you can also declare a group of examples with additional information that will be added to their JSON Schemas inside of OpenAPI.
"""
class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results