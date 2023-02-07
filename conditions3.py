last_name = input("last name: \n")
first_name = input("first name: \n")
gender = input("f/m: \n")

if gender == 'm':
    print("Hello, Mr. {0} {1}, nice to meet you!".format(last_name, first_name))
elif gender == 'f':
    print("Hello, Mrs. {0} {1}, nice to meet you!".format(last_name, first_name))
