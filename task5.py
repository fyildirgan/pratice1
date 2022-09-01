#pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
print(df.head())
df2 = pd.unique(df[['pclass', 'parch']].values.ravel())
print(df2)