import pandas as pd

df = pd.read_csv("Superstore.csv", encoding="latin1")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())

import pandas as pd

df = pd.read_csv("Superstore.csv", encoding="latin1")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df["Order Date"] = pd.to_datetime(df["Order Date"])

print(df.info())
print(df.head())

import matplotlib.pyplot as plt

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xticks(rotation=45)
plt.title("Monthly Sales")
plt.tight_layout()
plt.savefig("images/monthly_sales.png")
plt.show()