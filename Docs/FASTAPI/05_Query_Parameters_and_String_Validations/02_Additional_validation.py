from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

# Annotated[type, metadata]
@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {'items': [{'item_id':'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q':q})
    return results