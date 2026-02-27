from .DrugData import DrugValidData
import pandas as pd

def predict_drug_class(model, features : DrugValidData):
    

    predicted_class = model.predict(pd.DataFrame([features.model_dump()] ))

    return predicted_class[0]   


    
      
