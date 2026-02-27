from fastapi import APIRouter
from dotenv import load_dotenv
import os
 

router_predict = APIRouter()

load_dotenv()


@router_predict.get("/")
def health_check():
    app_name = os.getenv("APP_NAME")
    return {"Hello": f"World from {app_name}!"}

@router_predict.post("/predict")
def predict():
    return {"message": "This is the predict endpoint"}
