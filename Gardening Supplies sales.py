import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
file_path = "/mnt/data/dataset_23_Photography Services.csv"
df = pd.read_csv(file_path)

# Step 2: Filter Gardening Supplies sales
# Assuming there's a 'Category' column with product types and 'Sales' column for revenue
if 'Category' in df.columns and 'Sales' in df.columns:
    gardening_df = df[df['Category'] == 'Gardening Supplies']
else:
    print("Error: Relevant columns not found in the dataset.")
    exit()

# Step 3: Summary Statistics
print("Summary of Gardening Supplies Sales:")
print(gardening_df.describe())

# Total Sales
total_sales = gardening_df['Sales'].sum()
print(f"\nTotal Gardening Supplies Sales: {total_sales}")

# Average Sales per Product
average_sales = gardening_df['Sales'].mean()
print(f"Average Sales per Product: {average_sales}")

# Top-Selling Products
if 'Product Name' in gardening_df.columns:
    top_products = gardening_df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
    print("\nTop 5 Gardening Products:")
    print(top_products)

# Step 4: Visualization
# Total Sales by Month (assuming there's a 'Month' column)
if 'Month' in gardening_df.columns:
    monthly_sales = gardening_df.groupby('Month')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
    plt.title("Monthly Sales of Gardening Supplies")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Pie Chart for Top Products
if 'Product Name' in gardening_df.columns:
    top_products.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title="Top Gardening Supplies")
    plt.ylabel("")
    plt.show()

# Step 5: Save Cleaned Data
output_path = "/mnt/data/gardening_supplies_sales.csv"
gardening_df.to_csv(output_path, index=False)
print(f"\nCleaned Gardening Supplies data saved to: {output_path}")