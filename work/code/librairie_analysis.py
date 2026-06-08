import pandas as pd


def get_store_with_highest_revenue(file_path):
    sales_data = pd.read_csv(file_path)

    discount_rate = sales_data["Discount"] / 100
    sales_data["Revenue"] = (
            sales_data["Units_Sold"]
            * sales_data["Unit_Price"]
            * (1 - discount_rate)
    )

    store_revenue_totals = sales_data.groupby("Store")["Revenue"].sum()
    top_store = store_revenue_totals.idxmax()

    return top_store

def most_genre_hav_max_quantity(file_path):
    df = pd.read_csv(file_path)
    result = df.groupby("Genre")["Units_Sold"].sum().idxmax()
    return result


def most_actif_day(file_path):
    df = pd.read_csv(file_path)
    result = df.groupby("Date")["Units_Sold"].sum().idxmax()
    return result


def most_book_sold_out(file_path):
    df = pd.read_csv(file_path)
    result = df.groupby("Book_Title")["Units_Sold"].sum().idxmax()
    return result


def revenue_after_discount(file_path):
    df = pd.read_csv(file_path)
    df.add_prefix("test")
    print(df)


file_to_test = "E:/data_analyst/work/data/bookstore_sales.csv"
print(revenue_after_discount(file_to_test))
