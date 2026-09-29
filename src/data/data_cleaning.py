import pandas as pd 
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT/"data"/"raw"/"online_retail_II.xlsx"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_retail.csv"



df_2010 = pd.read_excel(DATA_PATH, sheet_name = "Year 2009-2010")
df_2011 = pd.read_excel(DATA_PATH, sheet_name = "Year 2010-2011")
df = pd.concat([df_2010, df_2011], ignore_index=True)

df["Invoice"] = df["Invoice"].astype(str)
df = df[~df["Invoice"].str.startswith("C")]

df = df[df["Customer ID"].notna()]

df = df[df["Price"] >= 0]

df = df.drop_duplicates()

df.to_csv(OUTPUT_PATH, index=False)


