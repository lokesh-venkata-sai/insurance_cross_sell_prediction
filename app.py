from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import yaml
import os

app = FastAPI()


class InputData(BaseModel):
    Gender: str
    Age: int
    HasDrivingLicense: int
    RegionID: float
    Switch: int
    PastAccident: str
    AnnualPremium: float


with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

model_file_path = os.path.join(config['model']['store_path'], config['model']['name'] + '_model.pkl')
model = joblib.load(model_file_path)


@app.get("/")
async def read_root():
    return {"health_check": "OK", "model_version": 3}


@app.post("/predict")
async def predict(input_data: InputData):
    df = pd.DataFrame([input_data.model_dump().values()],
                      columns=input_data.model_dump().keys())
    predicted = model.predict(df)
    return {"predicted_class": int(predicted[0])}
