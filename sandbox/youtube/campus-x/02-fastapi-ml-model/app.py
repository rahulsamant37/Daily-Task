from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

import pickle
import pandas as pd

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

## import the ml model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

## Pydatic Model
class UserInput(BaseModel):
    age:Annotated[int, Field(...,gt=0,le=120, description="This is the age of the Person should be between 0 to 120", example=21)]
    weight:Annotated[float, Field(...,gt=0, description="This is the weight of the peron in kg", example=119.8)]
    height:Annotated[float, Field(...,gt=0, description="This is the height of the peron in meters", example=1.56)]
    income_lpa:Annotated[float, Field(...,gt=0, description="This is the salary of the peron in CTC per annum", example=2.92)]
    smoker:Annotated[bool, Field(..., description="This is wether a person smokes or not", examples=[True,False])]
    city:Annotated[str, Field(..., description="This is the city of the Person where he/she lives", example='Jaipur')]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], Field(..., description="This is the occupation of the Person what he/she does for living", example='retired')]

    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        return "low"
    
    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

app = FastAPI()

@app.get("/")
def main():
    return {"message": "This is my ML model Prediction API"}

@app.post("/predict")
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'prediction': prediction})