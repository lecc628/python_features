
# Each object has an identity. An object’s identity never changes once it has been created; you may think of it
# as the object’s address in memory. The 'is' and 'is not' operators compare the identity and not identity
# of two objects; the id() function returns an integer representing its identity.

# CPython implementation detail: For CPython, id(x) is the memory address where x is stored.

# For immutable types, operations that compute new values may actually return a reference to any existing
# object with the same type and value, while for mutable objects this is not allowed.
# E.g., after a = 1; b = 1, a and b may or may not refer to the same object with the value one, depending on
# the implementation, but after c = []; d = [], c and d are guaranteed to refer to two different, unique,
# newly created empty lists. (Note that, c = d = [] assigns the same object to both c and d.)

# When you use the == operator:
#  - For immutable objects, it compares by identity.
#  - For mutable objects, it compares by value.

from typing import Tuple, List

def compare_object_identity() -> None:
    print("/********************************* Immutable object (int): *********************************/\n")
    int_1: int = 3
    int_2: int = 3
    print(f"{id(int_1) = }")             # id(int_1) = 140704421434216
    print(f"{id(int_2) = }")             # id(int_2) = 140704421434216
    print(f"{int_1 is int_2 = }\n")      # int_1 is int_2 = True

    print("/******************************** Immutable object (tuple): ********************************/\n")
    tuple_1: Tuple[int] = (1, 2, 3)
    tuple_2: Tuple[int] = (1, 2, 3)
    print(f"{id(tuple_1) = }")           # id(tuple_1) = 2277874983232
    print(f"{id(tuple_2) = }")           # id(tuple_2) = 2277874983232
    print(f"{tuple_1 is tuple_2 = }\n")  # tuple_1 is tuple_2 = True

    print("/********************************* Mutable object (list): **********************************/\n")
    list_1: List[int] = [1, 2, 3]
    list_2: List[int] = [1, 2, 3]
    print(f"{id(list_1) = }")            # id(list_1) = 2277842403712
    print(f"{id(list_2) = }")            # id(list_2) = 2277875099008
    print(f"{list_1 is list_2 = }\n")    # list_1 is list_2 = False


compare_object_identity()
