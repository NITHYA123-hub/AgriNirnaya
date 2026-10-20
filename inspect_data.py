import pandas as pd
from pathlib import Path

data_folder = Path("data")
master_file = data_folder / "crop_dataset.csv"

print("=" * 80)
print(f"MASTER DATASET: {master_file.name}")
print("=" * 80)

if master_file.exists():
    df = pd.read_csv(master_file, encoding="utf-8")
    print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nDistinct Crops:", df["crop"].nunique())
    print(df["crop"].unique())
    print("\nDistinct Districts:", df["district"].nunique())
    print("\nDistinct Categories:", df["category"].unique())
    print("\nMissing values:")
    print(df.isnull().sum()[df.isnull().sum() > 0])
else:
    print("Master dataset not found!")
