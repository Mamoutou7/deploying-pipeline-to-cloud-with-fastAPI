import pandas as pd
from sklearn.model_selection import train_test_split
import pytest
from fastapi.testclient import TestClient
from main import app
from starter.starter.ml.data import process_data


@pytest.fixture(scope="module")
def client():
    """Client for API testing"""
    client = TestClient(app)
    return client


@pytest.fixture(scope="module")
def path():
    return "starter/data/cleaned_census.csv"


@pytest.fixture(scope="module")
def load_data():
    """
    Load the dataset
    """
    path_data = "starter/data/cleaned_census.csv"
    return pd.read_csv(path_data)


@pytest.fixture(scope="module")
def features():
    """
    Fixture - will return the categorical features as argument
    """
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country"
    ]
    return cat_features

@pytest.fixture(scope="module")
def train_dataset(load_data, features):

    train, test = train_test_split(load_data,
                                   test_size=0.20,
                                    random_state=10,
                                    stratify=load_data['salary']
                                   )

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
    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    return X_train, y_train