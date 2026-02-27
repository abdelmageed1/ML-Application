from fastapi import FastAPI ,HTTPException
from dotenv import load_dotenv
import os
from src.utils.config import model_drug_classifier
from src.utils.DrugData import DrugValidData
from src.utils.inference import predict_drug_class
 
load_dotenv()  # Load environment variables from .env file


app = FastAPI()

@app.get("/")
def read_root():
    app_name = os.getenv("APP_NAME")
    return {"Hello": f"World from {app_name}!"}


@app.post("/predict")
def predict_new(data: DrugValidData):
  try:
    result = predict_drug_class(model_drug_classifier, data)
    return {"prediction": result}
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))