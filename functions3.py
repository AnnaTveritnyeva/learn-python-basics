price = int(input("Please enter the price"))


def get_price(number):
    dis = 0.1
    if number > 1000:
        dis = get_discount() / 100
    return number - number * dis


def get_discount():
    x = float(input("enter discount: "))
    return x


print(get_price(price))
