from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.gender)
    print(patient.age)
    print(patient.address.city)
    print(patient.address.state)
    print(patient.address.zip_code)
    print("Patient inserted successfully!")

# Example usage
address_dict = {"city": "Chandigarh", "state": "Chandigarh", "zip_code": "160012"}

address1 = Address(**address_dict)

patient_dict = {"name": "Rahul", "gender": "Male", "age": 22, "address": address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()
temp1 = patient1.model_dump(include=["name"])

print(temp)
print(temp1)
print(type(temp))