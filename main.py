import pickle
import json
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]    
)

#Load the model
model = pickle.load(open('Benglore_House_Price_model.pickle','rb'))
data_columns = json.load(open('columns.json', 'r'))['data_columns']
class HouseData(BaseModel):
    location : str
    total_sqft : float
    bath : int
    bhk : int

class PredictionResponse(BaseModel):
    predicted_price : float
    currency : str
    message : str
    
    
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request= request,
        name = 'index.html'
    )

@app.post("/predict", response_model = PredictionResponse)
def predict(data: HouseData):
    x = np.zeros(len(data_columns))

    x[0] = data.total_sqft
    x[1] = data.bath
    x[2] = data.bhk
    
    if data.location in data_columns:
        loc_idx = data_columns.index(data.location)
        x[loc_idx] = 1
        
        prediction = model.predict([x])[0]
    else:
        raise HTTPException(
            status_code = 400,
            detail = f"Location - '{data.location}' is not supported."
        )
        
    return {
        "predicted_price": round(prediction, 2),
        "currency":'Lakhs',
        "message": 'Prediction generated successfully.'
    }
