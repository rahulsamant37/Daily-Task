from fastapi import FastAPI
from controllers import router as patient_router

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Welcome to My Hospital App"}

@app.get("/about")
def about():
    return {"message": "This application is created by none other than Rahul for the Hospital"}

app.include_router(patient_router)