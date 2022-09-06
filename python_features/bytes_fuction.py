'''Contains examples about bytes fuction.'''


def use_bytes() -> None:
    print(bytes.__doc__, "\n")

    my_bytes_1 = b"abc"
    print(f"{type(my_bytes_1) = }")
    print(f"{my_bytes_1 = }")

    my_bytes_2 = bytes(b"abc")
    print(f"{type(my_bytes_2) = }")
    print(f"{my_bytes_2 = }")

    # A zero-filled bytes object of a specified length: bytes(5)
    my_bytes_3 = bytes(5)
    print(f"{type(my_bytes_3) = }")
    print(f"{my_bytes_3 = }")

    # From an iterable of integers: bytes(range(20))
    my_bytes_4 = bytes(range(20))
    print(f"{type(my_bytes_4) = }")
    print(f"{my_bytes_4 = }")

    # From an iterable of integers: bytes(range(256))
    my_bytes_5 = bytes(range(256))
    print(f"{type(my_bytes_5) = }")
    print(f"{my_bytes_5 = }")

    my_list = list(my_bytes_1)
    print(f"{my_list = }")


use_bytes()
