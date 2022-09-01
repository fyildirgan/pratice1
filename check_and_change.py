# embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
a = df.columns[0:2]
print(a)

print(df[["embarked", "survived"]])

df["embarked"] = df["embarked"].astype("category")

print(df["embarked"].dtype)
# print(df.columns)
