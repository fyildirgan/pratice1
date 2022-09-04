# Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df = df[df["sex"] == 'female']
df = df[df['age'] >= 40]
print(df.head)