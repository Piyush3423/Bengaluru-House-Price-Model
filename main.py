from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to Bengaluru House Price Prediction API"}

class HouseData(BaseModel):
    location : str
    total_sqrt : float
    bath : int
    bhk : int
