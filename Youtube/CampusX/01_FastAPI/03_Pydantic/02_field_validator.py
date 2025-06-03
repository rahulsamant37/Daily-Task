from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    allergirs: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if not value.endswith(".edu.in"):
            raise ValueError("Email must be a College email ending with .edu.in")
        return value
    
    @field_validator("name")
    @classmethod
    def first_letter_captial_name(cls, value):
        if not value[0].isupper():
            raise ValueError("Name must start with a capital letter")
        return value
    
    @field_validator("age", mode="before")## after type corection
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 120:
            return value
        else:
            raise ValueError("Age must be between 1 and 119")

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergirs)
    print(patient.contact_details)
    print("Patient inserted successfully!")

patient_info = {"name": "Rahul", "email": "abc@gmail.com.edu.in", "age": 30, "weight": 70.5, 
                "allergirs": ["pollen", "nuts"], 
                "contact_details": {"phone": "1234567890", "address": "123 Main St"}}
patient1= Patient(**patient_info)
insert_patient(patient1)