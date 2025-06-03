from fastapi import APIRouter, Path, HTTPException
from services import get_all_patients, get_patient_by_id

router = APIRouter()

@router.get("/view")
def view():
    return get_all_patients()

@router.get("/patient/{id}")
def view_one(id: str = Path(..., description="The ID of the patient to view", example="1")):
    patient = get_patient_by_id(id)
    if patient:
        return patient
    raise HTTPException(status_code=404, detail=f"Sorry there is no patient with this {id} id!")
