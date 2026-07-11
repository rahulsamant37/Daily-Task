from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Optional, Literal
import json

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f) ## This will take a dictonary and insert it into json

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

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None,gt=0)]
    gender: Annotated[Optional[Literal['Male', 'Female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None,gt=0)]
    weight: Annotated[Optional[float], Field(default=None,gt=0)]

    

app = FastAPI()

@app.get('/')
def main():
    return {'message':'Welcome to my Hostipal API'}

@app.put('/edit/{patient_id}')
def update_info(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='This patient don"t exists in data')
    
    existing_info = data[patient_id]
    updated_info = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_info.items():
        existing_info[key] = value
    
    # existing_info -> pydantic object -> updated bmi + verdict
    existing_info['id'] = patient_id
    patient_pydatic_obj = Patient(**existing_info)
    ## -> pydantic object -> dict
    existing_info = patient_pydatic_obj.model_dump(exclude='id')

    # Add this dict to data
    data[patient_id] = existing_info

    # Save data
    save_data(data)

    ## Response
    return JSONResponse(status_code=200, content={'message':'Your patient info is sucessfully updated!'})
