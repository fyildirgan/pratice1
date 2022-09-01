import seaborn as sns

df = sns.load_dataset("titanic")

# num_but_cat = [col for col in df.columns if df[col].unique() < 10]
a = []
for col in df.columns:
    x = df[col]
    y = x.nunique()
    if y < 10:
        a.append(col)
        print(a)
