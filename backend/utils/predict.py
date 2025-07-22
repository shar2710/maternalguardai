import pandas as pd
import joblib
from config.config import MODEL_PATHS
from utils.preprocessing import preprocess_data

def make_prediction(model_name, input_df):
    if model_name not in MODEL_PATHS:
        raise ValueError(f"Model '{model_name}' not found.")

    model = joblib.load(MODEL_PATHS[model_name])
    processed_df = preprocess_data(input_df)

    prediction = model.predict(processed_df).tolist()

    try:
        proba = model.predict_proba(processed_df).tolist()
    except:
        proba = None

    return {
        "predictions": prediction,
        "probabilities": proba
    }
