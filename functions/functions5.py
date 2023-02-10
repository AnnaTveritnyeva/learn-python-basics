def smalldiv(a, b):
    m = min(a, b)
    for i in range(2, m):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1


def biggest(a, b):
    m = min(a, b)
    for i in range(m, 1, -1):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1


def mypow(a, b):
    return pow(a, b)


def sqdiff(a, b):
    return pow(a, 0.5) - pow(b, 0.5)


a = int(input("enter a:"))
b = int(input("enter b:"))

d = {'a': biggest, 'b': smalldiv, 'c': mypow, 'd': sqdiff}

while True:
    print("a- the biggest devider")
    print("b- the smallest divider")
    print("c- the result of pow(a,b)")
    print("d- the result of sqrt(a)-sqrt(b)")
    print("e- exit")
    c = input("")
    if c == 'e':
        break
    print(d[c](a, b))
