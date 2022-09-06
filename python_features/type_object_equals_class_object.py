'''Contains examples about type object equals class object.'''


# The type object is the same object than the class object for a type.

class A:
    ...


a = A()
print(f"type(a) is A: {type(a) is A}\n")  # type(a) is A: True

NUM = 123
print(f"type(NUM) is int: {type(NUM) is int}\n")  # type(NUM) is int: True


# I you have a class instance, then you get the class object of that
# class using the special attribute __class__.

# a.__class__ is type(a): True
print("a.__class__ is type(a):", a.__class__ is type(a))
# a.__class__ is A: True
print("a.__class__ is A:", a.__class__ is A)
