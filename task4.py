#pclass değişkeninin unique değerlerinin sayısını bulunuz.
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("titanic")
print(df.head())
a = df["pclass"].unique()
print(a)