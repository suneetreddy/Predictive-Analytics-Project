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

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

monthly_df = monthly_sales.reset_index()
monthly_df.columns = ["Month", "Sales"]

monthly_df["Month_Number"] = range(len(monthly_df))

X = monthly_df[["Month_Number"]]
y = monthly_df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)