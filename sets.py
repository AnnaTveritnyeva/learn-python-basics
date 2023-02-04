ls1 = [10, 20, 30, 40, 50, 60]
ls2 = [3, 4, 5, 3, 7, 5, 9, 10, 20, 10]

print(set(ls2))
print(set(ls1) & set(ls2))

ls3 = ls1
ls3.remove(20)
ls3.remove(40)
print(ls3)

print(set(ls1)-set(ls2))
