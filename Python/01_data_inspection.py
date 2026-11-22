import pandas as pd
from pathlib import Path

# Project folder location
BASE_DIR = Path(__file__).resolve().parents[1]

# Original assignment data folder
DATA_DIR = BASE_DIR / "Arcass_Round2_ARC-2026-00050"

# List of CSV files
files = [
    "orders.csv",
    "order_items.csv",
    "customers.csv",
    "products.csv",
    "returns.csv",
    "price_history.csv",
    "cost_history.csv",
    "marketing_spend.csv",
    "answers.csv"
]

# Inspect each dataset
for file in files:

    print("\n" + "=" * 60)
    print("DATASET:", file)

    df = pd.read_csv(DATA_DIR / file)

    print("\nNumber of rows and columns:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nFirst five records:")
    print(df.head())


    print("\n========== ORDERS DATASET ==========")

df = pd.read_csv(DATA_DIR / "orders.csv")

print("\nFirst 10 records:")
print(df.head(10).to_string())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())