import pandas as pd
from pathlib import Path

# Original files are in the current folder
# Cleaned files will be saved one folder above, in Cleaned_Data
output_folder = Path("../Cleaned_Data")
output_folder.mkdir(exist_ok=True)

# Read datasets
orders = pd.read_csv("orders.csv")
items = pd.read_csv("order_items.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
returns = pd.read_csv("returns.csv")
prices = pd.read_csv("price_history.csv")
costs = pd.read_csv("cost_history.csv")
marketing = pd.read_csv("marketing_spend.csv")

# 1. Remove exact duplicate records
orders = orders.drop_duplicates().copy()
items = items.drop_duplicates().copy()

# 2. Standardize city names
city_mapping = {
    "bangalore": "Bengaluru",
    "blr": "Bengaluru",
    "bengaluru urban": "Bengaluru",
    "hyd": "Hyderabad",
    "bombay": "Mumbai",
    "new delhi": "Delhi",
    "ncr-delhi": "Delhi",
    "delhi": "Delhi",
    "pune": "Pune",
    "poona": "Pune",
    "amdavad": "Ahmedabad",
    "madras": "Chennai",
    "calcutta": "Kolkata",
    "lko": "Lucknow"
}

for df in [orders, customers]:
    df["city"] = (
        df["city"].str.strip().str.lower()
        .map(city_mapping)
        .fillna(df["city"].str.strip().str.title())
    )

# 3. Convert date columns
orders["order_ts"] = pd.to_datetime(orders["order_ts"])
customers["signup_date"] = pd.to_datetime(customers["signup_date"])
products["launch_date"] = pd.to_datetime(products["launch_date"])
returns["return_date"] = pd.to_datetime(returns["return_date"])
prices["effective_from"] = pd.to_datetime(prices["effective_from"])
costs["effective_from"] = pd.to_datetime(costs["effective_from"])

# 4. Standardize missing coupon values
orders["coupon_code"] = orders["coupon_code"].fillna("No Coupon")

# 5. Convert marketing spend into INR
marketing["spend_inr"] = marketing.apply(
    lambda row: row["spend"] * 100000
    if row["unit"] == "INR_lakh"
    else row["spend"],
    axis=1
)

# 6. Save cleaned datasets
datasets = {
    "orders_clean.csv": orders,
    "order_items_clean.csv": items,
    "customers_clean.csv": customers,
    "products_clean.csv": products,
    "returns_clean.csv": returns,
    "price_history_clean.csv": prices,
    "cost_history_clean.csv": costs,
    "marketing_spend_clean.csv": marketing
}

for filename, df in datasets.items():
    df.to_csv(output_folder / filename, index=False)
    print(filename, "saved | Rows:", len(df))

print("\n--- CLEANING SUMMARY ---")
print("Orders before cleaning: 12312")
print("Orders after cleaning:", len(orders))
print("Order items after cleaning:", len(items))
print("Marketing spend total INR:", marketing["spend_inr"].sum())
print("\nAll cleaned files saved successfully!")