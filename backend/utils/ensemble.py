import joblib
import pandas as pd
from collections import Counter
from config.config import MODEL_PATHS
from utils.preprocessing import preprocess_data

def load_models(model_names):
    models = []
    for name in model_names:
        if name in MODEL_PATHS:
            model = joblib.load(MODEL_PATHS[name])
            models.append((name, model))
        else:
            raise ValueError(f"Model '{name}' not found in config.")
    return models

def ensemble_predict(model_names, input_df):
    processed_df = preprocess_data(input_df)
    models = load_models(model_names)

    all_preds = []
    for _, model in models:
        preds = model.predict(processed_df)
        all_preds.append(preds)

    # Transpose to get predictions per sample
    all_preds = list(zip(*all_preds))  # shape: [n_samples][n_models]

    # Majority vote
    final_preds = []
    for sample_preds in all_preds:
        vote = Counter(sample_preds).most_common(1)[0][0]
        final_preds.append(vote)

    return {
        "ensemble_predictions": final_preds,
        "model_predictions": [list(p) for p in zip(*all_preds)]
    }
