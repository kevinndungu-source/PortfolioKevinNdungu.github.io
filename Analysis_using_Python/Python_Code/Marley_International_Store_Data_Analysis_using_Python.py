import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file

# Please note: If your're practising using this script, kindly change the location path to reflect your current location of the dataset.

file_path = r'C:\Users\ADMIN\Documents\Personal\Naivas\Marley International Store-2015.xlsx'
xls = pd.ExcelFile(file_path)

# Display sheet names to understand the structure of the file

sheet_names = xls.sheet_names
print(sheet_names)

# Load the Orders sheet into a DataFrame

orders_df = pd.read_excel(xls, sheet_name='Orders')

# Display the first few rows and the columns of the Orders DataFrame

print(orders_df.head())
print(orders_df.columns)

# Convert Order Date to datetime format
orders_df['Order Date'] = pd.to_datetime(orders_df['Order Date'])

# Extract month and year from Order Date
orders_df['Month'] = orders_df['Order Date'].dt.to_period('M')



# 1. Total Revenue Generated by the Store per Month

monthly_revenue = orders_df.groupby('Month')['Sales'].sum()
monthly_revenue.plot(kind='bar', figsize=(12, 6), title='Total Revenue per Month')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()



# 2. Category of Products Contributing the Most to Sales per Month

category_sales_monthly = orders_df.groupby(['Month', 'Product Category'])['Sales'].sum().unstack()
category_sales_monthly.plot(kind='bar', stacked=True, figsize=(12, 6), title='Monthly Sales by Product Category')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Product Category')
plt.show()



# 3. Sales Trend for the Past Year

monthly_revenue.plot(kind='line', marker='o', figsize=(12, 6), title='Sales Trend for the Past Year')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



# 4. Region with the Highest and Lowest Sales

region_sales = orders_df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar', figsize=(12, 6), title='Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.show()

highest_sales_region = region_sales.idxmax()
lowest_sales_region = region_sales.idxmin()

print(f'Highest Sales Region: {highest_sales_region}')
print(f'Lowest Sales Region: {lowest_sales_region}')



# 5. Average Profit Margin of the Store

total_profit = orders_df['Profit'].sum()
total_sales = orders_df['Sales'].sum()
average_profit_margin = (total_profit / total_sales) * 100

print(f'Average Profit Margin: {average_profit_margin:.2f}%')



# 6. Best Selling and Most Profitable Category

category_performance = orders_df.groupby('Product Category')[['Sales', 'Profit']].sum()
best_selling_category = category_performance['Sales'].idxmax()
most_profitable_category = category_performance['Profit'].idxmax()

print(f'Best Selling Category: {best_selling_category}')
print(f'Most Profitable Category: {most_profitable_category}')



# 7. Best Selling and Most Profitable Sub-Category

subcategory_performance = orders_df.groupby('Product Sub-Category')[['Sales', 'Profit']].sum()
best_selling_subcategory = subcategory_performance['Sales'].idxmax()
most_profitable_subcategory = subcategory_performance['Profit'].idxmax()

print(f'Best Selling Sub-Category: {best_selling_subcategory}')
print(f'Most Profitable Sub-Category: {most_profitable_subcategory}')



# 8. Top Selling Sub-Category

top_selling_subcategory = best_selling_subcategory
print(f'Top Selling Sub-Category: {top_selling_subcategory}')



# 9. Most Profitable Customer Segment

segment_profit = orders_df.groupby('Customer Segment')['Profit'].sum()
most_profitable_segment = segment_profit.idxmax()

print(f'Most Profitable Customer Segment: {most_profitable_segment}')



# 10. Preferred Ship Mode

ship_mode_preference = orders_df['Ship Mode'].value_counts()
ship_mode_preference.plot(kind='bar', figsize=(12, 6), title='Preferred Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()
preferred_ship_mode = ship_mode_preference.idxmax()

print(f'Preferred Ship Mode: {preferred_ship_mode}')



# 11. Most Profitable Region

region_profit = orders_df.groupby('Region')['Profit'].sum()
region_profit.plot(kind='bar', figsize=(12, 6), title='Total Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Profit')
plt.xticks(rotation=0)
plt.show()
most_profitable_region = region_profit.idxmax()

print(f'Most Profitable Region: {most_profitable_region}')



# 12. City with the Highest Number of Sales

city_sales_count = orders_df['City'].value_counts()
city_sales_count.head(10).plot(kind='bar', figsize=(12, 6), title='Top 10 Cities by Number of Sales')
plt.xlabel('City')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.show()
highest_sales_city = city_sales_count.idxmax()

print(f'City with the Highest Number of Sales: {highest_sales_city}')
