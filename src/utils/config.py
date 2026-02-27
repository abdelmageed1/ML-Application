from dotenv import load_dotenv
load_dotenv()
import joblib
import os

name_app = os.getenv('NAME_APP')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "drug_classifier.pkl")

model_drug_classifier = joblib.load(model_path)