import pandas as pd
from pathlib import Path
import numpy as np
from sklearn.preprocessing import StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "customer_features.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "customer_features_normalized.csv"

df = pd.read_csv(DATA_PATH)

# doing log transformation in order to reduce skewness
log_features = ["Frequency", "Monetary", "TotalQuantity", "UniqueProducts", "AverageOrderValue"]
df[log_features] = np.log1p(df[log_features])

# Normalizing features 
scaler = StandardScaler()
features = [
    "Recency",
    "Frequency",
    "Monetary",
    "TotalQuantity",
    "UniqueProducts",
    "AverageOrderValue"
]

scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

df.to_csv(OUTPUT_PATH, index=False)