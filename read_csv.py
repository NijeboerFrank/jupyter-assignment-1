import pandas as pd

file = "Assignment 23-09-2019 - Forensics - Sheet1.csv"

df = pd.read_csv(file)
df["Legal"] = df["Legal"].apply(str.capitalize)


