import pandas as pd

df = pd.read_csv("titanic.csv")
print("\nDuplicates count:-")
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates deleted!")
print("\nNull count:-")
print(df.isnull().sum())
print()
sample = df[(df["Age"]>39) & (df["Sex"]=="Female")]
print("Selected rovs:-\n")
print(sample)
print(df["Pclass"].describe())
df["Survived"] = 0
print("\nAdded 'Survived' column successfully!")
