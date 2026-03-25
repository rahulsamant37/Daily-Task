from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def get_patient_data():
    with open("PATH-QUERY_AND_HTTP/patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def main():
    return {"message": "Welcome to my Hospital API"}

@app.get("/about/")
def about():
    return {"message": "This is a simple API for managing hospital data."}

@app.get("/patients")
def get_patients():
    data = get_patient_data()
    return data

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example= "1")):
    data = get_patient_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by:str = Query(..., description="Sort patients by this age, height and weight", example="height"), 
                  order: str = Query("asc", description="Order of sorting", examples=["asc","desc"])):
    data = get_patient_data()
    if sort_by not in ["age", "height", "weight"]:
        raise HTTPException(status_code=400, detail="Invalid sort_by parameter for sort_by it can either be age, height or weight")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order parameter for order it can either be asc or desc")
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == "desc"))
    return sorted_data