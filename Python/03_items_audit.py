import pandas as pd

items = pd.read_csv("order_items.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")

print("\n--- ORDER ITEMS AUDIT ---")
print("Total rows:", len(items))
print("Exact duplicate rows:", items.duplicated().sum())

print("\n--- DUPLICATE ITEM RECORDS ---")
print(
    items[items.duplicated(keep=False)]
    .sort_values(["order_id", "line_no"])
    .head(20).to_string(index=False)
)

print("\n--- DUPLICATE ORDER + LINE NUMBERS ---")
print(
    "Duplicate order_id + line_no:",
    items.duplicated(subset=["order_id", "line_no"]).sum()
)

print("\n--- INVALID ORDER REFERENCES ---")
print(
    "Items linked to missing orders:",
    (~items["order_id"].isin(orders["order_id"])).sum()
)

print("\n--- INVALID PRODUCT REFERENCES ---")
print(
    "Items linked to missing SKUs:",
    (~items["sku"].isin(products["sku"])).sum()
)

print("\n--- QUANTITY AND PRICE VALIDATION ---")
print("Zero or negative quantities:", (items["qty"] <= 0).sum())
print("Zero or negative unit prices:", (items["unit_price"] <= 0).sum())
print("Negative line discounts:", (items["line_discount"] < 0).sum())

print("\n--- COMPLETED ---")