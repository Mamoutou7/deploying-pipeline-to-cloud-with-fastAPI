import os.path

from ml.data import process_data
from ml.model import compute_model_metrics, inference

def slice_categorical_feature(test, cat_features, col_name, trained_model, encoder, lb):
    """ Function for data slicing model performance given certain categorical column
    Inputs
    ------
        test: The test data processed
        cat_features: All categorical features
        col_name: Column name of the test data processed to slice
        trained_model:  Trained machine learning model.
        encoder : sklearn.preprocessing._encoders.OneHotEncoder
            Trained sklearn OneHotEncoder, only used if training=False.
        lb : sklearn.preprocessing._label.LabelBinarizer
            Trained sklearn LabelBinarizer, only used if training=False.
    """

    # Categorical features unique values
    unique_values = test[col_name].unique()
    #
    for col in unique_values:
        idx = test[col_name] == col
        test_temp = test[idx]
        # Processing this subset of data for testing
        X_test, y_test, encoder, lb = process_data(
            test_temp,
            categorical_features=cat_features,
            label="salary",
            training=False,
            encoder=encoder,
            lb=lb
        )

        # Inference
        preds = inference(trained_model, X_test)
        # Compute metrics
        precision, recall, fbeta = compute_model_metrics(y_test, preds)

        path_dir = os.path.dirname(__file__)
        with open(os.path.join(path_dir, '../screenshots/slice_data_outputs.txt'), 'w') as file:
            file.write(f"{col_name}\n")
            for val in unique_values:
                file.write(f"\t {val.strip()}\n")
                file.write(f"\t\t precision:{precision} recall:{recall} fbeta:{fbeta}\n")

