'''Contains examples about comprehension.'''


from typing import Callable, Any

print("\n/******************** List comprehension: **********************/\n")


def create_list_of_empty_lists(length: int, /) -> list[list[Any]]:
    return [[] for _ in range(length)]


def filter_list(
        list_: list[Any], predicate_: Callable[[Any], bool], /) -> list[Any]:
    return [elem for elem in list_ if predicate_(elem)]


def is_even(num: int, /) -> bool:
    return num % 2 == 0


list_of_0 = create_list_of_empty_lists(0)  # []
list_of_1 = create_list_of_empty_lists(1)  # [[]]
list_of_3 = create_list_of_empty_lists(3)  # [[], [], []]

print(f"{list_of_0 = }")  # list_of_0 = []
print(f"{list_of_1 = }")  # list_of_1 = [[]]
print(f"{list_of_3 = }\n")  # list_of_3 = [[], [], []]

list_0 = [i for i in range(11)]
print(f"{list_0 = }")  # list_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_1 = filter_list(list_0, is_even)
print(f"{list_1 = }")  # list_1 = [0, 2, 4, 6, 8, 10]

print("\n/******************** Dict comprehension: **********************/\n")
# TODO: Write examples here.

print("\n/******************** Set comprehension: ***********************/\n")
# TODO: Write examples here.
