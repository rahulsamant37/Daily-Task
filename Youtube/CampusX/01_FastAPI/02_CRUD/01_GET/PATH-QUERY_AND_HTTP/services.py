from typing import Dict, Optional
from models import Patient
from database import load_data, save_data

def get_all_patients() -> Dict[str, dict]:
    return load_data()

def get_patient_by_id(patient_id: str) -> Optional[dict]:
    data = load_data()
    return data.get(patient_id)
