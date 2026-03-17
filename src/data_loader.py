import pandas as pd

def load_data(file_path):
    try:
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        else:
            return pd.read_excel(file_path, engine="openpyxl")
    except Exception as e:
        print("Error loading file:", e)
        return None