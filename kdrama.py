import pandas as pd

df = pd.read_csv("kdrama.csv")

print(df)
title = input("Enter a Kdrama title: ").lower()

result = df[df["Title"].str.lower().str.contains(title)]

print(result)
