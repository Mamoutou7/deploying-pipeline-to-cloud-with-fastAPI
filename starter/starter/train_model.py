# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
import os
import pandas as pd
import joblib
from ml.model import train_model, compute_model_metrics, inference
from ml.data import process_data
from data_slicing import slice_categorical_feature

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)


# Add code to load in the data.
path_dir = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(path_dir, "../data/cleaned_census.csv"))

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split( test_size=0.20,
                                random_state=10,
                                stratify=data['salary']
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

# Process the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb
)

# Train and save a model.
trained_model  = train_model(X_train, y_train)
joblib.dump(trained_model, os.path.join(path_dir, '../model/model.joblib'))
joblib.dump(encoder, os.path.join(path_dir, '../model/encoder.joblib'))

# Data slicing function on "native-country" column
slice_categorical_feature(test, cat_features, "native-country", trained_model, encoder, lb)

# Show the overall performance for writing model card
preds = inference(trained_model, X_test)
precision, recall, fbeta = compute_model_metrics(y_test, preds)
print(f"Overall Performance: precision:{precision}, recall:{recall}, fbeta:{fbeta}")