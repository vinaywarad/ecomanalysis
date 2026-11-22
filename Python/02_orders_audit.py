import pandas as pd

# Load orders dataset
df = pd.read_csv("orders.csv")

print("\n--- BASIC INFORMATION ---")
print("Total rows:", len(df))

# 1. Check completely duplicate rows
print("\n--- FULL DUPLICATES ---")
print("Duplicate rows:", df.duplicated().sum())

# 2. Check duplicate order IDs
print("\n--- DUPLICATE ORDER IDs ---")
print("Duplicate order IDs:", df["order_id"].duplicated().sum())

print("\nDuplicate order records:")
print(
    df[df.duplicated(subset=["order_id"], keep=False)]
    .sort_values("order_id")
    .head(20).to_string(index=False)
)

# 3. Check order statuses
print("\n--- ORDER STATUSES ---")
print(df["order_status"].value_counts(dropna=False))

# 4. Check city names
print("\n--- CITY NAMES ---")
print(df["city"].value_counts(dropna=False))

# 5. Check channels
print("\n--- CHANNELS ---")
print(df["channel"].value_counts(dropna=False))

# 6. Check payment methods
print("\n--- PAYMENT METHODS ---")
print(df["payment_method"].value_counts(dropna=False))

# 7. Check dates
print("\n--- DATE VALIDATION ---")
dates = pd.to_datetime(df["order_ts"], errors="coerce")

print("Invalid dates:", dates.isna().sum())
print("Earliest date:", dates.min())
print("Latest date:", dates.max())

# 8. Check possible test orders
print("\n--- POSSIBLE TEST ORDERS ---")
print(df[
    df.astype(str).apply(
        lambda col: col.str.contains("test", case=False, na=False)
    ).any(axis=1)
].to_string(index=False))