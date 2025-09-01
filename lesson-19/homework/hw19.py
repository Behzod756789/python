top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling_product_per_category = top_products.groupby('Category').first().reset_index()

print(top_selling_product_per_category)


top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling_product_per_category = top_products.groupby('Category').first().reset_index()

print(top_selling_product_per_category)



sales_df['TotalSales'] = sales_df['Quantity'] * sales_df['Price']
daily_sales = sales_df.groupby('Date')['TotalSales'].sum().reset_index()
top_sales_day = daily_sales.loc[daily_sales['TotalSales'].idxmax()]

print(top_sales_day)


orders_df = pd.read_csv('task/customer_orders.csv')

order_counts = orders_df.groupby('CustomerID')['OrderID'].nunique()
frequent_customers = order_counts[order_counts >= 20].index

filtered_orders = orders_df[orders_df['CustomerID'].isin(frequent_customers)]
print(filtered_orders.head())



customer_avg_price = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
high_value_customers = customer_avg_price[customer_avg_price['Price'] > 120]

print(high_value_customers)



product_totals = orders_df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', lambda x: (x * orders_df.loc[x.index, 'Quantity']).sum())
).reset_index()

filtered_products = product_totals[product_totals['total_quantity'] >= 5]
print(filtered_products)


import sqlite3

conn = sqlite3.connect('task/population.db')

population_df = pd.read_sql_query("SELECT * FROM population", conn)

conn.close()



salary_bands_df = pd.read_excel('task/population salary analysis.xlsx')



def assign_salary_band(salary):
    for _, row in salary_bands_df.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Band']
    return 'Uncategorized'

population_df['SalaryBand'] = population_df['Salary'].apply(assign_salary_band)




salary_band_stats = population_df.groupby('SalaryBand').agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()

total_population = population_df.shape[0]
salary_band_stats['percentage_population'] = (salary_band_stats['population_count'] / total_population) * 100

print(salary_band_stats)



state_band_stats = population_df.groupby(['State', 'SalaryBand']).agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()

state_totals = population_df.groupby('State').size().reset_index(name='state_total')

state_band_stats = state_band_stats.merge(state_totals, on='State')
state_band_stats['percentage_population'] = (state_band_stats['population_count'] / state_band_stats['state_total']) * 100

print(state_band_stats)


