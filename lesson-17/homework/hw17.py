import pandas as pd
import numpy as np

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
print("1. Renamed Columns:")
print(df, "\n")

print("2. First 3 Rows:")
print(df.head(3), "\n")

print("3. Mean Age:", df['age'].mean(), "\n")

print("4. Name and City Columns:")
print(df[['first_name', 'City']], "\n")

df['Salary'] = np.random.randint(4000, 10000, size=len(df))
print("5. Added Salary Column:")
print(df, "\n")

print("6. Summary Statistics:")
print(df.describe(include='all'))



import pandas as pd

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Sales': [5000, 6000, 7500, 8000],
        'Expenses': [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data)

print("1. Sales and Expenses DataFrame:")
print(sales_and_expenses, "\n")

print("2. Maximum Sales:", sales_and_expenses['Sales'].max())
print("   Maximum Expenses:", sales_and_expenses['Expenses'].max(), "\n")

print("3. Minimum Sales:", sales_and_expenses['Sales'].min())
print("   Minimum Expenses:", sales_and_expenses['Expenses'].min(), "\n")

print("4. Average Sales:", sales_and_expenses['Sales'].mean())
print("   Average Expenses:", sales_and_expenses['Expenses'].mean())



import pandas as pd

data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
        'January': [1200, 200, 300, 150],
        'February': [1300, 220, 320, 160],
        'March': [1400, 240, 330, 170],
        'April': [1500, 250, 350, 180]}

expenses = pd.DataFrame(data)

expenses = expenses.set_index('Category')

print("1. Expenses DataFrame:")
print(expenses, "\n")

print("2. Maximum Expense by Category:")
print(expenses.max(axis=1), "\n")

print("3. Minimum Expense by Category:")
print(expenses.min(axis=1), "\n")

print("4. Average Expense by Category:")
print(expenses.mean(axis=1))

