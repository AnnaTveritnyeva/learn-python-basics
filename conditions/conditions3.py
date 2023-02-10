last_name = input("last name: \n")
first_name = input("first name: \n")
gender = input("f/m: \n")

if gender == 'm':
    s = "Mr."
else:
    s = "Mrs"

print("Hello, Mr. {0} {1} {2}, nice to meet you!".format(s, last_name, first_name))
