import numpy as np
from .config import SUMMARY_TXT, HIGH_SALES_THRESHOLD

def print_summary(df):
    print("Unique Products:", df['Product'].unique())
    print("Average Sale:", np.mean(df['Total_Sales']))
    print("Max Sale:", np.max(df['Total_Sales']))

def get_high_sales(df):
    return df[df['Total_Sales'] > HIGH_SALES_THRESHOLD]

def save_summary_to_file(df):
    SUMMARY_TXT.parent.mkdir(parents=True, exist_ok=True)
    with open(SUMMARY_TXT, "w") as f:
        f.write(f"Unique Products: {df['Product'].unique()}\n")
        f.write(f"Average Sale: {np.mean(df['Total_Sales'])}\n")
        f.write(f"Max Sale: {np.max(df['Total_Sales'])}\n")
