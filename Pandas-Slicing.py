import pandas as pd

data = {
    'Student_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print(df.iloc[1:3, 1:])
