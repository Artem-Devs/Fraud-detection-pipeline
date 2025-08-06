from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load the model and scaler
model = joblib.load('models/tuned_lightgbm_model.pkl')
scaler = joblib.load('models/standard_scaler.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse incoming JSON as a list of records
        data = request.get_json()

        # Convert list of dicts into DataFrame
        input_df = pd.DataFrame(data)

        # Scale features
        scaled = scaler.transform(input_df)

        # Predict classes and probabilities
        preds = model.predict(scaled)
        probs = model.predict_proba(scaled)[:, 1]

        # Prepare response
        results = []
        for pred, prob in zip(preds, probs):
            results.append({
                "predicted_class": int(pred),
                "fraud_probability": float(prob)
            })

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
