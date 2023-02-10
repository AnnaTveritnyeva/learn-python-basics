name = input("Name: ")

cust_file = open('cust.csv')
cust_file_list = cust_file.readlines()
cust_file.close()


def find_id():
    for i in range(1, len(cust_file_list)):
        temp_list = cust_file_list[i].split(',')
        if temp_list[1] == name:
            id_num = temp_list[0]
            return find_total_orders(id_num)
    return "Not found"


def find_total_orders(id_num):
    total_orders = 0
    orders_file = open('orders.csv')
    orders_file_list = orders_file.readlines()
    orders_file.close()
    for i in range(1, len(orders_file_list)):
        temp_list = orders_file_list[i].split(',')
        if temp_list[1] == id_num:
            total_orders += int(temp_list[3])
    return total_orders


print("Total: ", find_id())
