import json
from typing import Dict
from models import Patient

DATA_FILE = "patients.json"

def load_data() -> Dict[str, dict]:
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data: Dict[str, dict]):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
