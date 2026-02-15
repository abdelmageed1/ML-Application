from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os


# قاعدة المسار بالنسبة لملف main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# مسار الموديل الصحيح
MODEL_PATH = os.path.join(BASE_DIR, "models", "final_pipeline.pkl")
MODEL_PATH = os.path.abspath(MODEL_PATH)

# print("Base directory:", BASE_DIR)
# print("Model path:", MODEL_PATH)
# # تحقق أن الملف موجود
# print("Model exists:", os.path.exists(MODEL_PATH))




model = joblib.load(MODEL_PATH)

 


app = FastAPI(title="Bank Churn Prediction API")


# # ===============================
# # 4️⃣ Define Input Schema
# # ===============================
class CustomerData(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


# ===============================
# 5️⃣ Home Route
# ===============================
@app.get("/")
def home():
    return {"message": "Bank Churn Model API is running "}


# # ===============================
# # 6️⃣ Prediction Route
# # ===============================
@app.post("/predict")
def predict(data: CustomerData):

    # Convert input to DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": float(round(probability, 4))
    }










