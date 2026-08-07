def checkArmstrong(num):
    if num < 0:
        return False
    temp = num
    total = 0
    power = len(str(num))
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return num == total

number = int(input("Enter a number: "))
print(checkArmstrong(number))
