
# - The assertions are evaluated if the __debug__ constant value is True. By default its value is True.
# - If you execute the interpreter with the option -O (optimization), then the __debug__ constant value
# is False and the assertions are ignored.

MIN_VALUE: int = 8

a: int = 5
print(a)

assert a > MIN_VALUE, f'The value of "a" must be greater than {MIN_VALUE}.'

# The above assertion is semantically equivalent to the following code:

if __debug__:
    if not a > MIN_VALUE:
        raise AssertionError(f'The value of "a" must be greater than {MIN_VALUE}.')
