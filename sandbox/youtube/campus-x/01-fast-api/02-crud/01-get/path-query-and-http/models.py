from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Annotated

class Patient(BaseModel):
    id: Annotated[str, Field( description="Unique identifier for the patient")]
    name: Annotated[str, Field(min_length=1, max_length=50, description="Name of the patient")]
    age: Annotated[int, Field(ge=0, le=120, description="Age of the patient")]
    diagnosis: Annotated[str, Field(min_length=1, max_length=100, description="Diagnosis of the patient")]

    @field_validator('age')
    @classmethod
    def check_age(cls, value):
        if not 0 < value < 120:
            raise ValueError("Age must be between 0 and 120")
        return value

    @model_validator(mode='after')
    def check_diagnosis(cls, model):
        if model.age>100 and model.diagnosis.lower() != "critical":
            raise ValueError("Patients over 100 with diagnosis cannot have a diagnosis other than 'critical'")
        return model
        