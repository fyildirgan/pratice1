# embarked değeri C olanların tümbilgelerini gösteriniz.
import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
from matplotlib import pyplot as plt

df = sns.load_dataset("titanic")
#df = df[["embarked", "age"]]
#print(df)

indexList = df.index
for i in indexList:
    embarked_value =df["embarked"].get(i)
    if 'C' != embarked_value:
        df = df.drop(i)
print(df)
