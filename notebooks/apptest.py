import requests
import joblib
import pandas as pd
X_test = joblib.load('../data/X_test.pkl')

# Sample test data (use the same columns as in training)
sample = X_test.iloc[:2].to_dict(orient='records')

# POST to the API
response = requests.post("http://127.0.0.1:5000/predict", json=sample)

# Show result
print(response.json())
