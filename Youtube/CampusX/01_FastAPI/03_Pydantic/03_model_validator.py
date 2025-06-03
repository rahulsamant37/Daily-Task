from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    allergirs: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode="after") 
    def validate_bmi(cls, model):
        if model.age > 60 and model.weight < 50:
            raise ValueError("BMI is too low for patients over 60 years old.")
        return model

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergirs)
    print(patient.contact_details)
    print("Patient inserted successfully!")

patient_info = {"name": "Rahul", "email": "abc@gmail.com.edu.in", "age": 70, "weight": 70.5, 
                "allergirs": ["pollen", "nuts"], 
                "contact_details": {"phone": "1234567890", "address": "123 Main St"}}
patient1= Patient(**patient_info)
insert_patient(patient1)