fruits = {"apple", "banana", "orange", "mango", "grape", "kiwi", "pear", "peach", "plum", "cherry"}
summer_fruits = {"mango", "watermelon", "lychee", "peach", "plum", "Pineapple"}
winter_fruits = {"apple", "orange", "kiwi", "grape", "pomegranate"}

print(fruits | summer_fruits | winter_fruits)

print(fruits & winter_fruits)

print(summer_fruits - fruits)

print((summer_fruits & winter_fruits) - fruits)

print("orange" in fruits)

if "Pineapple" in fruits:
    print("fruits")
elif "Pineapple" in summer_fruits:
    print("summer_fruits")
elif "Pineapple" in winter_fruits:
    print("winter_fruits")
