from fastapi.testclient import TestClient
from main import app
import json

# Instantiate the testing client with our app.
client = TestClient(app)


def test_api_locally_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"greeting" : "Welcome to the census data prediction platform!"}


def test_api_locally_model_inference_x():
    """
    Test for POST method for model Inference prediction with output ">50K"
    """
    data_sample = {
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
    response = client.post(
        "/predict/",
        data=json.dumps(data_sample),
    )

    assert response.status_code == 200
    assert response.json()["prediction"] == ">50K"


def test_api_locally_model_inference_y():
    """
     Test for POST method for model Inference prediction with output "<=50K"
     """
    data_sample = {
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
        "native_country": "United-States"
    }

    response = client.post(
        "/predict/",
        data=json.dumps(data_sample),
    )
    assert response.status_code == 200
    assert response.json()["prediction"] == "<=50K"