employees = ("Alice", "Bob", "Alice", "Charlie", "David", "Eve", "Bob", "Frank", "Grace", "Alice", "Heidi", "Ivan", "Judy", "Frank", "Eve", "Charlie", "Alice", "David", "Grace", "Judy")

for name in set(employees):
    print(name, employees.count(name))

distinct_employees = tuple(set(employees))
print(len(distinct_employees))

max_freq_name = max(set(employees), key=employees.count)
print(max_freq_name)

sorted_employees = sorted(distinct_employees)
print(sorted_employees)

search_name = input("Enter employee name: ")
print(search_name in employees)
