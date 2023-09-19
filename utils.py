import pandas as pd

def generate_dataframe():
    csv_file_path = 'penguins.csv'
    return pd.read_csv(csv_file_path)