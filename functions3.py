price = int(input("Please enter the price"))


def expensive(number):
    if number > 1000:
        dis = int(input("Please enter discount"))
        return discount(number, dis)
    return number * 0.9


def discount(num, dis):
    return num * (1 - dis / 100)


print(expensive(price))
