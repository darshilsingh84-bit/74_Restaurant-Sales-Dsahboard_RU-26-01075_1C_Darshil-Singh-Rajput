import pandas as pd
import matplotlib.pyplot as plt



file_name = "restaurant.csv"

try:
    df = pd.read_csv(file_name, dtype=str)

except FileNotFoundError:
    print("Error: File 'restaurant.csv' not found.")
    exit()




required_columns = ["Date", "Item", "Category", "Quantity", "Price"]

for col in required_columns:
    if col not in df.columns:
        print("Error: Required column is missing.")
        exit()


df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")



for index, row in df.iterrows():

    if pd.isna(row["Quantity"]):
        print("Warning: Row", index + 2,
              "skipped - Quantity must be a number.")

    elif pd.isna(row["Price"]):
        print("Warning: Row", index + 2,
              "skipped - Price must be a number.")



df = df.dropna(subset=["Quantity", "Price"])



df["Sales"] = df["Quantity"] * df["Price"]


print("\n===== RESTAURANT SALES DASHBOARD =====")

print("1. Sales by Category")
print("2. Top Items")
print("3. Top Items and Daily Sales")

choice = input("Enter your choice: ")



if choice == "1":

    category_sales = df.groupby("Category")["Sales"].sum()

    print("\nSales by Category:")

    for category, sales in category_sales.items():
        print(category, ": Rs.", int(sales))

    total_sales = df["Sales"].sum()

    print("Total sales: Rs.", int(total_sales))



    category_sales.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    plt.show()



elif choice == "2":

    item_quantity = df.groupby("Item")["Quantity"].sum()

    item_revenue = df.groupby("Item")["Sales"].sum()

    top_quantity = item_quantity.idxmax()
    top_revenue = item_revenue.idxmax()

    print("\nTop Items:")

    print("Top item by quantity:",
          top_quantity,
          "(", int(item_quantity[top_quantity]), "units)")

    print("Top item by revenue:",
          top_revenue,
          "(Rs.", int(item_revenue[top_revenue]), ")")



    item_quantity.plot(kind="bar")

    plt.title("Top Items by Quantity")
    plt.xlabel("Items")
    plt.ylabel("Quantity")

    plt.show()



elif choice == "3":

    item_quantity = df.groupby("Item")["Quantity"].sum()

    item_revenue = df.groupby("Item")["Sales"].sum()

    top_quantity = item_quantity.idxmax()
    top_revenue = item_revenue.idxmax()

    print("\nTop item by quantity:",
          top_quantity,
          "(", int(item_quantity[top_quantity]), "units)")

    print("Top item by revenue:",
          top_revenue,
          "(Rs.", int(item_revenue[top_revenue]), ")")



    daily_sales = df.groupby("Date")["Sales"].sum()

    print("\nDaily Sales:")

    for date, sales in daily_sales.items():
        print(date, ": Rs.", int(sales))



    best_day = daily_sales.idxmax()

    print("Best day:", best_day)

  

    daily_sales.plot(kind="bar")

    plt.title("Daily Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.show()


else:

    print("Invalid choice! Please enter 1, 2 or 3.")
