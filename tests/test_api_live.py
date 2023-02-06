import requests


api_url = "https://deploying-pipeline-with-fastapi.onrender.com"

input_sample = {
    "age": 30,
    "workclass": "State-gov",
    "fnlgt": 141297,
    "education": "Bachelors",
    "education_num": 13,
    "marital_status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "Asian-Pac-Islander",
    "sex": "Male",
    "capital_gain": 0,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": "India"
}
response = requests.post( api_url +
    "/predict",
    json=input_sample
)

print(f"Input: {input_sample}")
print(f"Prediction: {response.content}")
