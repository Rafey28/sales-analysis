from src.data_processing import load_data, create_total_sales, save_data
from src.analysis import print_summary, get_high_sales, save_summary_to_file
from src.visualization  import (
    plot_total_sales_per_product,
    plot_daily_sales_trends,
    plot_units_sold_over_time
)

def main():
    df = load_data()
    df = create_total_sales(df)
    save_data(df)

    print_summary(df)
    high_sales_df = get_high_sales(df)
    print("High Sales Records:\n", high_sales_df)

    save_summary_to_file(df)

    plot_total_sales_per_product(df)
    plot_daily_sales_trends(df)
    plot_units_sold_over_time(df)

if __name__ == "__main__":
    main()
