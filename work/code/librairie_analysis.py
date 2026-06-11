import pandas as pd


# 1 Quel magasin a généré le plus de chiffre d'affaires ?
def get_store_with_highest_revenue(file_path):
    sales_data = pd.read_csv(file_path)
    discount_rate = sales_data["Discount"] / 100
    sales_data["Revenue"] = (
            sales_data["Units_Sold"]
            * sales_data["Unit_Price"]
            * (1 - discount_rate)
    )
    top_store = sales_data.groupby("Store")["Revenue"].sum().idxmax()
    return top_store


# 2 Quel genre de livre se vend le mieux en quantité ?
def most_genre_hav_max_quantity(file_path):
    sales_data = pd.read_csv(file_path)
    return sales_data.groupby("Genre")["Units_Sold"].sum().idxmax()


# 3 Quel jour de la semaine semble le plus actif (extrapoler avec la date) ?
def most_actif_week(file_path):
    sales_data = pd.read_csv(file_path)
    return sales_data.groupby("Date")["Units_Sold"].sum().idxmax()


# 4 Quel livre a la meilleure performance en volume ?
def most_book_sold_out(file_path):
    sales_data = pd.read_csv(file_path)
    return sales_data.groupby("Book_Title")["Units_Sold"].sum().idxmax()


# 5 Calculez le revenu total après discount pour chaque transaction
def revenue_after_discount(file_path):
    sales_data = pd.read_csv(file_path)
    discount_rate = sales_data["Discount"] / 100
    sales_data["Revenue"] = (
            sales_data["Units_Sold"]
            * sales_data["Unit_Price"]
            * (1 - discount_rate)
    )

    return sales_data["Revenue"]


# 6 Quel magasin vend le plus de livres pour enfants ?
def get_store_with_highest_sale_children_book(file_path):
    children_book = "Children"
    sales_data = pd.read_csv(file_path)
    sales_data_children = sales_data[sales_data["Genre"] == children_book]
    return sales_data_children.groupby("Store")["Units_Sold"].sum().idxmax()

# 7 Quel est le livre le moins vendu ?
def get_book_with_bad_revenue(file_path):
    sales_data = pd.read_csv(file_path)
    return sales_data.groupby("Book_Title")["Units_Sold"].sum().idxmin()


file_to_test = "E:/data_analyst/work/data/bookstore_sales.csv"
print(get_book_with_bad_revenue(file_to_test))
