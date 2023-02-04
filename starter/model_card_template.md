# Model Card
This model card describes about the income prediction model trained on census income dataset.

## Model Details
* Developer: Mamoutou FOFANA
* Model date: 02/02/2023
* Model Version: 1.0.0
* Model type: DecisionTreeClassifier from scikit-learn

## Intended Use
* Primary intended uses: Predict if income is over 50K or under 50K.
* Primary intended users: Economy or sociology researcher.
* Out-of-scope use cases: Try to predict actual income or threshold that is not 50K.

## Training Data
Build a binary classification model to predict whether income exceeds $50K/yr based on census data. Also known as "Adult" dataset.
* training data split: 80% of total samples are randomly chosen to train a model
* Remove all extra space in string
* All categorical column are encoded using OneHotEncoder from scikit-learn
* Label column ('salary') is encoded using LabelBinarizer from scikit-learn

## Evaluation Data
* test data split: 20% of total samples are randomly chosen to test a model
* Remove all extra space in string
* All categorical column are encoded using OneHotEncoder from scikit-learn
* Label column ('salary') is encoded using LabelBinarizer from scikit-learn

## Metrics
Model's performance on those metrics
  - precision: 0.797
  - recall: 0.525
  - fbeta: 0.635

## Ethical Considerations
* The model is not intended to inform decisions about matters central to human life or flourishing – e.g., health or safety.
* Non-sensitive information

## Caveats and Recommendations
This model might be poor in performance:
* marital-status
* relationship

Check in /screenshots/slice_data_outputs.txt to find data slicing analysis scores.