
# The type object is the same object than the class object for a type.

class A: ...

a = A()
print("type(a) is A: {0}\n".format(type(a) is A))  # type(a) is A: True

num = 123
print("type(num) is int: {0}\n".format(type(num) is int))  # type(num) is int: True


# I you have a class instance, then you get the class object of that class using the special attribute __class__.

print("a.__class__ is type(a):", a.__class__ is type(a))  # a.__class__ is type(a): True
print("a.__class__ is A:", a.__class__ is A)  # a.__class__ is A: True
