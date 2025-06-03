from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50, description="Name of the patient must be between 3 and 50 characters")] 
    email: Annotated[EmailStr, Field(description="Email of the patient must be a valid email address")]
    age: Annotated[int, Field(gt=0, le=120, description="Age of the patient must be between 0 and 120")]
    weight: Annotated[Optional[int], Field(default=None, gt=0, strict=True, description="Weight of the patient must be greater than 0, optional field")]
    allergies: Annotated[List[str], Field(default=[], description="List of allergies the patient has, optional field")]
    contact_details: Annotated[Dict[str, str], Field(description="Contact details of the patient, must contain email and phone number")]

def insert_patient(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Patient inserted successfully")

Pantient_info = {"name": "Rahul", "email": "abc@gmail.com", "age": "22", "weight": 70,
                 "allergies": ["pollen", "dust"],
                 "contact_details": {"email": "abc@gmail.com","phone": "1234567890"}}

patient1 = Patient(**Pantient_info)
insert_patient(patient1)