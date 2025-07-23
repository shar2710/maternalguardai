import os
import pandas as pd
import joblib
from config.config import MODEL_PATHS
from utils.preprocessing import preprocess_data

def make_prediction(model_name, input_df):
    if model_name not in MODEL_PATHS:
        raise ValueError(f"Model '{model_name}' not found in MODEL_PATHS.")

    model_path = MODEL_PATHS[model_name]
    abs_path = os.path.abspath(model_path)

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"Model file not found at: {abs_path}")

    print(f"[DEBUG] Loading model from: {abs_path}")

    model = joblib.load(abs_path)
    processed_df = preprocess_data(input_df)

    prediction = model.predict(processed_df).tolist()

    try:
        proba = model.predict_proba(processed_df).tolist()
    except Exception as e:
        print(f"[DEBUG] Predict_proba failed: {e}")
        proba = None

    return {
        "predictions": prediction,
        "probabilities": proba
    }
