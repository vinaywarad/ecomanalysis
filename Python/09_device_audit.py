import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

print("\n========== DUPLICATED DEVICE IDS ==========")

device_counts = customers.groupby("device_id").agg(
    account_count=("customer_id", "nunique"),
    customer_ids=("customer_id", lambda x: ", ".join(x))
).reset_index()

shared_devices = device_counts[
    device_counts["account_count"] > 1
].sort_values("account_count", ascending=False)

print(shared_devices.to_string(index=False))

print("\n========== DUPLICATED PHONE HASHES ==========")

phone_counts = customers.groupby("phone_hash").agg(
    account_count=("customer_id", "nunique"),
    customer_ids=("customer_id", lambda x: ", ".join(x))
).reset_index()

shared_phones = phone_counts[
    phone_counts["account_count"] > 1
].sort_values("account_count", ascending=False)

print(shared_phones.to_string(index=False))

print("\n========== ORDERS BY SHARED DEVICE ==========")

if not shared_devices.empty:
    shared_customer_ids = customers[
        customers["device_id"].isin(shared_devices["device_id"])
    ]

    device_orders = orders.merge(
        shared_customer_ids[["customer_id", "device_id"]],
        on="customer_id",
        how="inner"
    )

    summary = device_orders.groupby("device_id").agg(
        accounts=("customer_id", "nunique"),
        orders=("order_id", "nunique"),
        coupons=("coupon_code", lambda x: ", ".join(
            sorted(x.dropna().astype(str).unique())
        )),
        statuses=("order_status", lambda x: ", ".join(
            sorted(x.dropna().astype(str).unique())
        ))
    ).reset_index()

    print(summary.to_string(index=False))

print("\n========== CUSTOMER ACCOUNTS ==========")
print(customers.to_string(index=False))