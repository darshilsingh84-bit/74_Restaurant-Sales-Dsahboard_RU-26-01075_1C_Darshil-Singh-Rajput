import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV File

file_name = "restaurant.csv"

try:
    df = pd.read_csv(file_name, dtype=str)

except FileNotFoundError:
    print("Error: File 'restaurant.csv' not found.")
    exit()


# Step 2: Check and Clean Data

required_columns = ["Date", "Item", "Category", "Quantity", "Price"]

for col in required_columns:
    if col not in df.columns:
        print("Error: Required column is missing.")
        exit()

# Convert Quantity and Price into numbers

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Find invalid rows

for index, row in df.iterrows():

    if pd.isna(row["Quantity"]):
        print("Warning: Row", index + 2,
              "skipped - Quantity must be a number.")

    elif pd.isna(row["Price"]):
        print("Warning: Row", index + 2,
              "skipped - Price must be a number.")

# Remove invalid rows

df = df.dropna(subset=["Quantity", "Price"])

# Step 3: Calculate Sales

df["Sales"] = df["Quantity"] * df["Price"]


# Step 4: Show Menu

print("\n===== RESTAURANT SALES DASHBOARD =====")

print("1. Sales by Category")
print("2. Top Items")
print("3. Top Items and Daily Sales")

choice = input("Enter your choice: ")


# Step 5: Sales by Category

if choice == "1":

    category_sales = df.groupby("Category")["Sales"].sum()

    print("\nSales by Category:")

    for category, sales in category_sales.items():
        print(category, ": Rs.", int(sales))

    total_sales = df["Sales"].sum()

    print("Total sales: Rs.", int(total_sales))

    # Graph

    category_sales.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    plt.show()


# Step 6: Top Items

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

    # Graph

    item_quantity.plot(kind="bar")

    plt.title("Top Items by Quantity")
    plt.xlabel("Items")
    plt.ylabel("Quantity")

    plt.show()


# Step 7: Top Items and Daily Sales

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

    # Daily Sales

    daily_sales = df.groupby("Date")["Sales"].sum()

    print("\nDaily Sales:")

    for date, sales in daily_sales.items():
        print(date, ": Rs.", int(sales))

    # Best Day

    best_day = daily_sales.idxmax()

    print("Best day:", best_day)

    # Graph

    daily_sales.plot(kind="bar")

    plt.title("Daily Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.show()


else:

    print("Invalid choice! Please enter 1, 2 or 3.")
