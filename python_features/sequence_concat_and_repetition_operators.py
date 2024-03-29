'''Contains examples about sequence concat and repetition operators.'''


# When you use the sequence concat operator, sequence_1 + sequence_2,
# or the sequence repetition operator, sequence * n or n * sequence, note that
# items in the result sequences are not copied; they are referenced multiple
# times (1); this means that:
#  - If item value is a mutable object, and you modify the value of the object,
#    then all references to that object will be modified.
#  - If item value is an immutable object, then you can NOT modify the value
#    of the object, you can only modify the item itself with a new completely
#    object.
# (1) Items are referenced multiple times because in Python each thing is
# an object, and the object is a type by reference (not by value).

class ClassWithInteger:
    '''Represents a simple class to use in the examples.'''

    def __init__(self, num: int) -> None:
        self.num = num

    def __str__(self) -> str:
        return f"{type(self).__name__}({str(self.num)})"

    def __repr__(self) -> str:
        return self.__str__()


def sequence_concat_operator() -> None:
    list_1 = [ClassWithInteger(1), ClassWithInteger(2)]
    print(f"{list_1 = }")     # list_1 = [ClassWithInteger(1), ClassWithInteger(2)]
    list_2 = [ClassWithInteger(3), ClassWithInteger(4)]
    print(f"{list_2 = }")     # list_2 = [ClassWithInteger(3), ClassWithInteger(4)]
    list_3 = list_1 + list_2  # Note that items from the sequences 'list_1' and 'list_2' are not copied; they are referenced multiple times.
    print(f"{list_3 = }\n")   # list_3 = [ClassWithInteger(1), ClassWithInteger(2), ClassWithInteger(3), ClassWithInteger(4)]
    list_1[0].num = 999       # Item value is a mutable object, and you modify the value of the object, then all references to that object will be modified.
    print(f"{list_1 = }")     # list_1 = [ClassWithInteger(999), ClassWithInteger(2)]
    print(f"{list_2 = }")     # list_2 = [ClassWithInteger(3), ClassWithInteger(4)]
    print(f"{list_3 = }\n")   # list_3 = [ClassWithInteger(999), ClassWithInteger(2), ClassWithInteger(3), ClassWithInteger(4)]

    list_4 = [1, 2, 3]
    print(f"{list_4 = }")     # list_4 = [1, 2, 3]
    list_5 = [4, 5, 6]
    print(f"{list_5 = }")     # list_5 = [4, 5, 6]
    list_6 = list_4 + list_5  # Note that items from the sequences 'list_4' and 'list_5' are not copied; they are referenced multiple times.
    print(f"{list_6 = }\n")   # list_6 = [1, 2, 3, 4, 5, 6]
    list_4[0] = 999           # Item value is an immutable object, then you can NOT modify the value of the object, you can only modify the item itself with a new completely object.
    print(f"{list_4 = }")     # list_4 = [999, 2, 3]
    print(f"{list_5 = }")     # list_5 = [4, 5, 6]
    print(f"{list_6 = }\n")   # list_6 = [1, 2, 3, 4, 5, 6]


def sequence_repetition_operator() -> None:
    empty_list = []
    print(f"Item value is a mutable object (empty list): {empty_list}")  # Item value is a mutable object (empty list): []
    list_1 = [empty_list] * 3  # Note that items in the sequence '[[]]' are not copied; they are referenced multiple times.
    print(f"{list_1 = }")    # list_1 = [[], [], []]
    list_1[0].append(3)      # Item value is a mutable object, and you modify the value of the object, then all references to that object will be modified.
    print(f"{list_1 = }\n")  # list_1 = [[3], [3], [3]]

    class_with_integer = ClassWithInteger(10)
    print(f"Item value is a mutable object (user-defined type): {class_with_integer}")  # Item value is a mutable object (user-defined type): ClassWithInteger(10)
    list_2 = [class_with_integer] * 3  # Note that items in the sequence '[ClassWithInteger(10)]' are not copied; they are referenced multiple times.
    print(f"{list_2 = }")    # list_2 = [ClassWithInteger(10), ClassWithInteger(10), ClassWithInteger(10)]
    list_2[1].num = 999      # Item value is a mutable object, and you modify the value of the object, then all references to that object will be modified.
    print(f"{list_2 = }\n")  # list_2 = [ClassWithInteger(999), ClassWithInteger(999), ClassWithInteger(999)]

    num = 1
    print(f"Item value is an immutable object ({type(num).__name__}): {num}")  # Item value is an immutable object (int): 1
    list_3 = [num] * 3       # Note that items in the sequence '[1]' are not copied; they are referenced multiple times.
    print(f"{list_3 = }")    # list_3 = [1, 1, 1]
    list_3[2] = 5            # Item value is an immutable object, then you can NOT modify the value of the object, you can only modify the item itself with a new completely object.
    print(f"{list_3 = }\n")  # list_3 = [1, 1, 5]


print("/**************** Using sequence concat operator: ****************/\n")
sequence_concat_operator()
print("/************* Using sequence repetition operator: ***************/\n")
sequence_repetition_operator()
