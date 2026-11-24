import pandas as pd
import os

folder = "irula_dataset"

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".parquet"):
            file_path = os.path.join(root, file)

            print("\nFile:", file)

            df = pd.read_parquet(file_path)

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nFirst 5 rows:")
            print(df.head())