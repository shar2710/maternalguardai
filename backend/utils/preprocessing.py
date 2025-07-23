import pandas as pd
import numpy as np

FEATURE_COLUMNS = [
    "blood_pressure_systolic", "blood_pressure_diastolic", "urine_protein",
    "platelet_count", "liver_enzymes", "serum_creatinine", "bmi", "age",
    "height_cm", "weight_kg", "white_blood_cell_count", "glucose_level",
    "body_temperature", "respiratory_rate", "gestational_age_weeks", "fetal_heart_rate",
    "urine_creatinine", "red_blood_cell_count", "parity", "hemoglobin", "heart_rate",
    "uterine_artery_pi", "PlGF_level", "sFlt1_PlGF_ratio", "mean_arterial_pressure",
    "preeclampsia"
]


def preprocess_data(df):
    X = df[FEATURE_COLUMNS].copy()
    X = X.fillna(X.median(numeric_only=True))
    
    return X
