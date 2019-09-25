import pandas as pd

file = "Assignment 23-09-2019 - Forensics - Sheet1.csv"

df = pd.read_csv(file)
df["Legal"] = df["Legal"].apply(str.capitalize)
df.groupby('Category')
grouped_cats = df.groupby(['Category', 'Legal']).size().unstack()
for grou in grouped_cats.iteritems():
    print(grou)
print(grouped_cats)

