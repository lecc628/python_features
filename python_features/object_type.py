'''Contains examples about object type.'''


# print(type(class_object)) = <class 'type'>
# If class_instance is an instance of a user-defined type.
# print(type(class_instance)) = <class 'QualifiedClassName'>
# If class_instance is an instance of a built-in type (int, list, etc.).
# print(type(class_instance)) = <class 'ClassName'>

class MyClass:
    def __str__(self) -> str:
        return f"{type(self).__name__}()"


list_0 = [1, 2, 3]
print(f"{list_0 = }")  # list_0 = [1, 2, 3]

m1 = MyClass()
# print function uses the __str__() for getting an informal string that
# represents its argument(s).
print("m1 =", m1)  # m1 = MyClass()
# f-string uses the __repr__() (not the __str__()) for getting a formal string
# that represents its interpolated value(s).
print(f"{m1 = }")  # m1 = <__main__.MyClass object at 0x000001CA70DD2A90>

print("\n/***************************************************************/\n")
print(f"{type(MyClass) = }")    # type(MyClass) = <class 'type'>
print(f"{type(MyClass()) = }")  # type(MyClass()) = <class '__main__.MyClass'>
print(f"{type(int) = }")        # type(int) = <class 'type'>

print("\n/***************************************************************/\n")
list_1 = [MyClass, MyClass, MyClass]
# The list's __str__() uses the __repr__() (not the __str__()) of its items
# for getting a string representation (formal string).
# list_1 = [
#   <class '__main__.MyClass'>,
#   <class '__main__.MyClass'>,
#   <class '__main__.MyClass'>
# ]
print(f"{list_1 = }")
list_2 = [MyClass(), MyClass(), MyClass()]
# list_2 = [
#   <__main__.MyClass object at 0x000001CA6EF12B90>,
#   <__main__.MyClass object at 0x000001CA6EF07210>,
#   <__main__.MyClass object at 0x000001CA6EF07350>
# ]
print(f"{list_2 = }")

print("\n/***************************************************************/\n")
# list_2 = [MyClass(), MyClass(), MyClass()]
print("list_2 = [", ", ".join([str(elem) for elem in list_2]), "]", sep="")
