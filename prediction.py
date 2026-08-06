import pandas as pd

df = pd.read_csv("Superstore.csv", encoding="latin1")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())