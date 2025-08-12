import pandas as pd
from .config import DATA_FILE, SUMMARY_FILE

def load_data():
    """Load sales data from CSV."""
    return pd.read_csv(DATA_FILE)

def create_total_sales(df):
    """Add Total_Sales column."""
    df['Total_Sales'] = df['Units_Sold'] * df['Unit_Price']
    return df

def save_data(df):
    """Save updated DataFrame to CSV."""
    SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SUMMARY_FILE, index=False)
