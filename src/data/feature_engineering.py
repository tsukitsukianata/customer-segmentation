import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT/"data"/"processed"/"cleaned_retail.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "customer_features.csv"

df = pd.read_csv(DATA_PATH)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["TotalPrice"] = df["Quantity"]*df["Price"]
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = (df.groupby("Customer ID") 
       .agg({
    "InvoiceDate": "max",
    "Invoice": "nunique",
    "TotalPrice": "sum",
    "Quantity": "sum",
    "StockCode": "nunique"
})
       .rename(columns = {
           "InvoiceDate":"Recency",
           "Invoice":"Frequency", 
           "TotalPrice":"Monetary",
           "Quantity":"TotalQuantity",
           "StockCode":"UniqueProducts"
       }))

rfm["Recency"] = (snapshot_date - rfm["Recency"]).dt.days
rfm["AverageOrderValue"] = rfm["Monetary"] / rfm["Frequency"]


rfm.reset_index().to_csv(OUTPUT_PATH, index=False)