from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def get_patient_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def main():
    return {"message": "Welcome to my Hospital API"}

@app.get("/search")
def search_patient(sort_by: str = Query(..., description="Sort patient by age, gender or weight", examples=['age','gender','weight']), order: str = Query("asc", description="sort order: asc or desc", examples=["asc", "desc"])):
    valid_field = ["age", "gender", "weight"]
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail="Invalid sort_by parameter for sort_by, must be either age, gender or weight")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order parameter for order, must be either 'asc' or 'desc'")
    data = get_patient_data()
    sorted_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse= sorted_order)
    return sorted_data