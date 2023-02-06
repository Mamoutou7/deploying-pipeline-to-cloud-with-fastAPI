# Put the code for your API here.
import os
import pandas as pd
import numpy as np
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Initialize FastAPI instance
app = FastAPI(
    title="Census API",
    description="An API that predict if income is over 50K or under 50K.",
    version="1.0.0")

# Declare the data object with its components and their type.
class DataSample(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: float
    capital_loss: float
    hours_per_week: float
    native_country: str


    class Config:
        schema_extra = {
            "example" : {
                "age": 38,
                "workclass": "private",
                "fnlgt": 215646,
                "education": "HS-grad",
                "education_num": 9,
                "marital_status": "Divorced",
                "occupation": "Handlers-cleaners",
                "relationship": "Not-in-family",
                "race": "White",
                "sex": "Male",
                "capital_gain": 0,
                "capital_loss": 0,
                "hours_per_week": 40,
                "native_country": "United-States",
            }
        }


# GET on the root giving a welcome message
@app.get("/")
async def welcome():
    return {"greeting": "Welcome to the census data prediction platform!"}

# This allows sending of data (our DataSample) via POST to the API.
@app.post("/predict")
async def model_inference(data: DataSample):

    path_file = os.path.dirname(__file__)
    model = joblib.load(os.path.join(path_file, "starter/model/model.joblib"))
    encoder = joblib.load(os.path.join(path_file, "starter/model/encoder.joblib"))

    # Replacing by the hyphen
    sample = {}
    for feature in data:
        sample[feature[0].replace("_", "-")] = [feature[1]]
    sample = pd.DataFrame.from_dict(sample)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X_categorical = sample[cat_features].values
    X_continuous = sample.drop(*[cat_features], axis=1)
    X_categorical = encoder.transform(X_categorical)
    X = np.concatenate([X_continuous, X_categorical], axis=1)

    # Inference
    pred = model.predict(X)
    result = "<=50K" if pred[0] == 0 else ">50K"

    # turn prediction into JSON
    return {"prediction": result}

