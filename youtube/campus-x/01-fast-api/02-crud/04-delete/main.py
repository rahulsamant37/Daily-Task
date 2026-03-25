from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated

import json

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f) ## This will take a dictonary and insert it into json

app = FastAPI()

@app.get('/')
def main():
    return {'messages':'Welcome! This is my Hospital API'}

@app.delete('/delete/{patient_id}')
def delete(patient_id: str):

    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='This patient don"t exist in our database')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200,content={'message':'Your Patient detail is sucessfully delete from our database!'})