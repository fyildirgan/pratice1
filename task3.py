#Her bir sutuna ait unique değerlerin sayısını bulunuz
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("titanic")
print(df.head())
df2 = pd.unique(df[['sex', 'age','survived']].values.ravel())
print(df2)