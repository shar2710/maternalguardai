import pandas as pd

def preprocess_data(df: pd.DataFrame):
    df = df.copy()
    df = df.fillna(0)  
    return df
