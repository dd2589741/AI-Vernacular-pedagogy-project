import os
import pandas as pd

dataset_folder = "dataset/irula_dataset"

for root, dirs, files in os.walk(dataset_folder):

    for file in files:

        if file.endswith(".parquet"):

            file_path = os.path.join(root, file)

            print("\n" + "=" * 60)
            print("FILE:", file_path)

            df = pd.read_parquet(file_path)

            print("\nRows:", len(df))

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nSample data:")

            for _, row in df.head(2).iterrows():

                for column in df.columns:

                    value = row[column]

                    if column == "audio":
                        print("Audio: Available")
                    else:
                        print(column, ":", value)

                print("-" * 40)