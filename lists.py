ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(ls[1])

print(ls[-1])

print(ls[::-1])

ls.sort()
print(ls)

print(ls.count(2))

list2 = input("Please enter 3 numbers")
ls += (list2.split(" "))
print(ls)

index1 = int(input("please enter index"))
ls.remove(ls[index1])
print(ls)

index2 = int(input("please enter index"))
ls[index2:index2] = []  # doesn't work
print(ls)
