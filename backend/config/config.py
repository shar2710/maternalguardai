import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "models", "saved_models")  

MODEL_PATHS = {
    "LogisticRegression": os.path.join(MODEL_DIR, "LogisticRegression.pkl"),
    "RandomForest": os.path.join(MODEL_DIR, "RandomForest.pkl"),
    "SVM": os.path.join(MODEL_DIR, "SVM.pkl"),
    "XGBoost": os.path.join(MODEL_DIR, "XGBoost.pkl"),
}
