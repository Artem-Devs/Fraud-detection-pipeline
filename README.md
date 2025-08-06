Credit Card Fraud Detection API

🚀 A machine learning pipeline for detecting fraudulent credit card transactions using LightGBM, with a Flask-powered API for real-time predictions. Based on publicly available Kaggle dataset.

📊 Dataset

This project uses the Credit Card Fraud Detection dataset from Kaggle.It includes over 280,000 anonymized transactions made by European cardholders in September 2013.

492 fraud cases (0.17%)

Features: 30 total (Time, Amount, V1 to V28, Class)

Target: Class (1 = Fraud, 0 = Normal)

🔍 Project Overview

Goal: Detect fraud in credit card transactions with high precision/recall.

Model: LightGBM Classifier (tuned with class weighting)

Preprocessing:

Remove duplicates

Standard scaling with StandardScaler

Train-test split with stratification

Deployment: Flask API for real-time predictions

🚀 Features

End-to-end ML pipeline (cleaning, training, testing, saving models)

Flask-based REST API

JSON input/output for model predictions

Uses saved scaler/model for consistent inference

Well-documented and clean code structure

