from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import Annotated
import json

class Patient(BaseModel):
    id: Annotated[str, Field(...,description="This is the ID of the existing patient from Hospital", example='1')]
    name: Annotated[str, Field(default='Guest',description="This is the Name of the Patient", example='Rahul')]
    city: Annotated[str, Field(...,description="This is the city of the patient", example='Chandigarh')]
    age: Annotated[int, Field(...,ge=0,le=120,description='It should be between 0 to 120',example=22)]
    gender: Annotated[str, Field(...,description='It can be male or female',examples=['Male', 'Female'])]
    height: Annotated[float, Field(...,gt=0, description='This is the height of the patient in meters', example=1.78)]
    weight: Annotated[float, Field(...,gt=0, description='This is the weight of the patient in kg', example=90)]

    @field_validator('age')
    @classmethod
    def check_age(cls, value):
        if 0 <= value <=120:
            return value
        else:
            raise ValueError('Your age must be between 0 to 120')
    
    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight / (self.height**2),2)
    
    @computed_field
    @property
    def verdit(self)->str:
        if self.bmi <= 18.5:
            return 'Underweight'
        elif 18.5 < self.bmi <= 25:
            return 'Normal weight'
        elif 25 < self.bmi <= 30:
            return 'Overweight'
        elif self.bmi > 30:
            return 'Obese'
    
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f) ## This will take a dictonary and insert it into json

app = FastAPI()

@app.get("/")
def main():
    return {"message":"Welcome to my Hostipal API"}

@app.post("/create")
def create_patient(patient: Patient):
    ## Load the data
    data = load_data()
    ## check if the patient exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists in data base')
    ## New patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    ## Save into the database
    save_data(data)

    ## Send the response
    return JSONResponse(status_code=201, content={'messages':'Your data is sucessfully saved in the database!'})