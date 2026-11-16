import pandas as pd

data = {
    'employee_id': [1, 2, 3, 4, 5],
    'employee_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Project_A_Contact': ['9876543210', None, '8765432109', '7654321098', None],
    'Project_B_Contact': [None, '6543210987', '5432109876', None, '4321098765']
}

df_wide = pd.DataFrame(data)
print("Wide Format:")
print(df_wide)
print("\n")

df_long = df_wide.melt(
    id_vars=['employee_id', 'employee_name'],
    value_vars=['Project_A_Contact', 'Project_B_Contact'],
    var_name='project_location',
    value_name='contact_no'
)

print("Long Format:")
print(df_long.dropna())
