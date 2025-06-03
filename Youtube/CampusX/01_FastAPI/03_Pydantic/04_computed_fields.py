from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    allergirs: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.allergirs)
    print(patient.contact_details)
    print("Patient inserted successfully!")

patient_info = {"name": "Rahul", "email": "abc@gmail.com.edu.in", "age": 70, "weight": 70.5, "height": 1.75,
                "allergirs": ["pollen", "nuts"], 
                "contact_details": {"phone": "1234567890", "address": "123 Main St"}}
patient1= Patient(**patient_info)
insert_patient(patient1)