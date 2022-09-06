'''Contains examples about printing list and tuple.'''


def print_list_tuple() -> None:
    dif_type_list = [123, 'aaa', None]
    print(f"List = {dif_type_list}")
    for elem in dif_type_list:
        print(type(elem))

    print()

    dif_type_tuple = (123, 'aaa', None)
    print(f"Tuple = {dif_type_tuple}")
    for elem in dif_type_tuple:
        print(type(elem))


print_list_tuple()
