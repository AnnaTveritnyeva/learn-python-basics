num = 0

while num != -999:
    digits = 0
    while num != 10:
        num //= 10
        digits += 1
    print(digits)
    num = int(input("Please enter number"))



