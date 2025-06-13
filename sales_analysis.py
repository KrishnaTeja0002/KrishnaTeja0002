import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV exported from MySQL
file_path = r"C:\Users\pc\sales analysis project\Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding='latin1')

# Group by Region to calculate total Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()

print(sales_by_region)  # ✅ Check output

# Plot Bar Chart
plt.figure(figsize=(8,5))
plt.bar(sales_by_region['Region'], sales_by_region['Sales'], color='skyblue')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Total Sales by Region')
plt.tight_layout()
plt.show()

profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()

plt.figure(figsize=(8,5))
plt.bar(profit_by_region['Region'], profit_by_region['Profit'], color='green')
plt.xlabel('Region')
plt.ylabel('Total Profit')
plt.title('Total Profit by Region')
plt.tight_layout()
plt.show()

sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()

plt.figure(figsize=(8,5))
plt.bar(sales_by_category['Category'], sales_by_category['Sales'], color='orange')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Total Sales by Category')
plt.tight_layout()
plt.show()

top_products = df.groupby('Product Name')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_products['Product Name'], top_products['Sales'], color='purple')
plt.xlabel('Total Sales')
plt.title('Top 10 Products by Sales')
plt.gca().invert_yaxis()  # highest sales at top
plt.tight_layout()
plt.show()

sales_by_region.to_csv(r'C:\Users\pc\sales analysis project\sales_by_region_output.csv', index=False)
profit_by_region.to_csv(r'C:\Users\pc\sales analysis project\profit_by_region_output.csv', index=False)

