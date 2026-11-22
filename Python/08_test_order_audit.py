import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

print("\n========== CUSTOMER COLUMNS ==========")
print(customers.columns.tolist())

print("\n========== ORDER COLUMNS ==========")
print(orders.columns.tolist())

print("\n========== POSSIBLE TEST ORDERS ==========")

for col in orders.select_dtypes(include="object").columns:
    mask = orders[col].astype(str).str.contains(
        "test|dummy|internal", case=False, na=False
    )

    if mask.any():
        print(f"\nColumn: {col}")
        print(orders.loc[mask].to_string(index=False))

print("\n========== CUSTOMER DEVICE INFORMATION ==========")
print(customers.head(10).to_string(index=False))

print("\n========== CUSTOMER ACCOUNT PATTERNS ==========")

for col in customers.select_dtypes(include="object").columns:
    mask = customers[col].astype(str).str.contains(
        "test|dummy|internal", case=False, na=False
    )

    if mask.any():
        print(f"\nColumn: {col}")
        print(customers.loc[mask].to_string(index=False))