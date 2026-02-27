from pydantic import BaseModel ,Field
from typing import  Literal 

class DrugValidData(BaseModel):
    Age : int = Field( gt=0, description="Age must be a positive integer")
    Sex  : Literal['F','M'] = Field(description="Gender must be either 'F' or 'M'")
    BP: Literal['HIGH','LOW','NORMAL'] = Field(description="Blood pressure must be either 'HIGH', 'LOW', or 'NORMAL'")
    Cholesterol: Literal['HIGH','NORMAL'] = Field(description="Cholesterol must be either 'HIGH' or 'NORMAL'")
    Na_to_K: float = Field(gt=0,description="Sodium to Potassium ratio")