# embarked değeri S olmayanların tüm bilgelerini gösteriniz.
import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
#print(df["embarked"])

#a = df[(df['embarked'] == 'C') | (df['embarked'] == 'Q')]
#b = df[df["embarked"] != 'S']
c = df[df['embarked'].isin(['C', 'Q'])]
#print(a)
#print(b)
print(c)
