import pandas as pd

def save_processed_data(df, path):
    df.to_csv(path, index=False)

def load_processed_data(path):
    return pd.read_csv(path)
