import pandas as pd
import numpy as np

FEATURE_COLUMNS = [
    "age", "gestational_age", "bmi", "systolic_bp", "diastolic_bp", "mean_arterial_pressure",
    "pulse_pressure", "serum_creatinine", "serum_uric_acid", "uric_acid_creatinine_ratio",
    "blood_urea_nitrogen", "alt_sgpt", "ast_sgot", "ldh", "hemoglobin", "hematocrit",
    "platelet_count", "white_blood_cell_count", "proteinuria_24h", "protein_creatinine_ratio",
    "serum_albumin", "fasting_glucose", "chronic_hypertension", "diabetes", "gestational_diabetes",
    "nulliparous", "multiple_pregnancy", "family_history_preeclampsia", "previous_preeclampsia",
    "autoimmune_disease", "chronic_kidney_disease", "thrombophilia", "headache",
    "visual_disturbance", "epigastric_pain", "nausea_vomiting", "shortness_of_breath",
    "swelling_edema", "decreased_urine_output", "altered_mental_status", "severe_hypertension",
    "thrombocytopenia", "elevated_liver_enzymes", "renal_dysfunction", "hellp_syndrome",
    "intrauterine_growth_restriction", "preterm_delivery", "placental_abruption",
    "label", "severity"
]


def preprocess_data(df):
    X = df[FEATURE_COLUMNS].copy()
    X = X.fillna(X.median(numeric_only=True))
    
    return X
