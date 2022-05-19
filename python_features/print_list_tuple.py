
def print_list_tuple():
    dif_type_list = [123, 'aaa', None]
    print("List: {}".format(dif_type_list))
    for elem in dif_type_list:
        print(type(elem))

    print()

    dif_type_tuple = (123, 'aaa', None)
    print("Tuple: {}".format(dif_type_tuple))
    for elem in dif_type_tuple:
        print(type(elem))

print_list_tuple()
