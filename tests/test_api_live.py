import requests

# Enter render web app here
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
# post to API and collect response
response = requests.post( api_url +
    "/predict",
    json=input_sample
)
# Validation code
print(f"Response status code: {response.status_code}")
# Show sample details
print(f"Input: {input_sample}")
# Model prediction added
print(f"Prediction: {response.content}")
