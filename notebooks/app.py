from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load('models/tuned_lightgbm_model.pkl')
scaler = joblib.load('models/standard_scaler.pkl')

# Define expected feature order
expected_columns = [
    "Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9",
    "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18",
    "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28",
    "Amount"
]

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Turn input into DataFrame and enforce column order
        input_df = pd.DataFrame([data])[expected_columns]

        # Scale and predict
        scaled = scaler.transform(input_df)
        preds = model.predict(scaled)
        probs = model.predict_proba(scaled)[:, 1]

        return jsonify({
            'predictions': preds.tolist(),
            'fraud_probabilities': probs.tolist()
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
