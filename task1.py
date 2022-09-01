#Seaborn kütüphanesi içerisinden Titanicveri setini tanımlayınız.
#Titanic verisetindekikadınveerkekyolcularınsayısınıbulunuz.
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("titanic")
#print(df.head())
a = df["sex"].value_counts()
#print(a)
