import matplotlib.pyplot as plt
import seaborn as sns
from .config import CHARTS_DIR

sns.set_theme(style="whitegrid", font_scale=1.2)
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'

def plot_total_sales_per_product(df):
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)

    ax = sns.barplot(x=product_sales.index, y=product_sales.values, palette="viridis", edgecolor="black")
    ax.set_title("Total Sales per Product", fontsize=16)
    ax.set_xlabel("Product", fontsize=14)
    ax.set_ylabel("Sales", fontsize=14)

    for p in ax.patches:
        ax.annotate(f"{p.get_height():,.0f}",
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "product_sales.png", dpi=300)
    plt.close()

def plot_daily_sales_trends(df):
    daily_sales = df.groupby('Date')['Total_Sales'].sum()
    daily_sales.plot(kind='line', color='royalblue', linewidth=2)
    plt.title("Daily Sales Trends", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Sales", fontsize=14)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "daily_sales_trends.png", dpi=300)
    plt.close()

def plot_units_sold_over_time(df):
    units_over_time = df.groupby(['Date', 'Product'])['Units_Sold'].sum().unstack()
    units_over_time.plot(kind='line', linewidth=2)
    plt.title("Units Sold Over Time by Product", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Units Sold", fontsize=14)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "units_sold_over_time.png", dpi=300)
    plt.close()
