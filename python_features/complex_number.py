
# - When converting from a string, the string must not contain whitespace around the central + or - operator.
# For example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError exception.
#
# - For a general Python object x, complex(x) delegates to x.__complex__(). If __complex__() is not defined
# then it falls back to __float__(). If __float__() is not defined then it falls back to __index__().

def print_complex(num: complex, name: str = "", is_conjugate: bool = False, /) -> None:
    if is_conjugate:
        print(f"{name} = {num}\tReal part = {num.real}\tImag part = {num.imag}\n")
    elif num.real == 0.0 and name == "":
        print(f"{name} = {num}\t\t\tReal part = {num.real}\tImag part = {num.imag}")
    else:
        print(f"{name} = {num}\t\tReal part = {num.real}\tImag part = {num.imag}")

def operate_complex_from_float(real: float = 0.0, imag: float = 0.0, name: str = "", /) -> None:
    num = complex(real, imag)
    print_complex(num, name)
    num_conjugate = num.conjugate()
    print_complex(num_conjugate, name + "_conjugate", True)

def operate_complex_from_str(num_as_string: str, name: str = "", /) -> None:
    operate_complex_from_float((num := complex(num_as_string)).real, num.imag, name)

def use_complex() -> None:
    operate_complex_from_float()
    operate_complex_from_float(1, 2, "z_1")
    operate_complex_from_float(3, 4)
    operate_complex_from_str("5+6j", "z_2")
    operate_complex_from_str("7+8j")

    operate_complex_from_float(0, 1)
    operate_complex_from_float(1, 0)
    operate_complex_from_float(2)
    operate_complex_from_str("0+3j")
    operate_complex_from_str("3+0j")
    operate_complex_from_str("4")
    operate_complex_from_str("5j")


use_complex()
