def doSum(num):
    total = 0
    num = abs(num)
    while num > 0:
        total += num % 10
        num //= 10
    return total

number = int(input("Enter a number: "))
print(doSum(number))
