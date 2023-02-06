"""
Unit test of model.py module with pytest
author: Mamoutou Fofana
Date: Jan. 6th 2023
"""

import pandas as pd
import pytest, os, logging, joblib
from sklearn.exceptions import NotFittedError

from starter.starter.ml.model import inference, compute_model_metrics

"""
Test methods
"""
def test_load_data(path):
    """
    Test presence and shape of dataset file
    """
    try:
        df = pd.read_csv(path)

    except FileNotFoundError as err:
        logging.error("File not found")
        raise err

    # Check the df shape
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0

    except AssertionError as err:
        logging.error(
        "Testing load_data: The file doesn't appear to have rows and columns")
        raise err


def test_features(load_data, features):
    """
    Check that categorical features are in dataset
    """
    try:
        assert sorted(set(load_data.columns).intersection(features)) == sorted(features)
    except AssertionError as err:
        logging.error(
        "Testing dataset: Features are missing in the data columns")
        raise err


def test_is_model():
    """
    Check saved model is present
    """
    savepath = "../starter/model/model.joblib"
    if os.path.isfile(savepath):
        try:
            _ = joblib.load(open(savepath, 'rb'))
        except Exception as err:
            logging.error(
            "Testing saved model: Saved model does not appear to be valid")
            raise err
    else:
        pass


def test_is_fitted_model(train_dataset):
    """
    Check saved model is fitted
    """

    X_train, y_train = train_dataset
    savepath = "../starter/model/model.joblib"
    model = joblib.load(open(savepath, 'rb'))

    try:
        model.predict(X_train)
    except NotFittedError as err:
        logging.error(
        f"Model is not fit, error {err}")
        raise err


def test_inference(train_dataset):
    """
    Check inference function
    """
    X_train, y_train = train_dataset

    savepath = "../starter/model/model.joblib"
    if os.path.isfile(savepath):
        model = joblib.load(open(savepath, 'rb'))

        try:
            preds = inference(model, X_train)
            logging.info(f"SUCCESS: prediction: {preds}")
        except Exception as err:
            logging.error(
            "Inference cannot be performed on saved model and train data")
            raise err
    else:
        pass


def test_compute_model_metrics(train_dataset):
    """
    Checking the performance metrics function
    """
    X_train, y_train = train_dataset

    savepath = "../starter/model/model.joblib"
    if os.path.isfile(savepath):
        model = joblib.load(open(savepath, 'rb'))
        preds = inference(model, X_train)

        try:
            precision, recall, fbeta = compute_model_metrics(y_train, preds)
            logging.info(f"SUCCESS: precision: {precision}, recall: {recall}, fbeta: {fbeta}")
        except Exception as err:
            logging.error(
            "Performance metrics cannot be calculated on train data")
            raise err
    else:
        pass