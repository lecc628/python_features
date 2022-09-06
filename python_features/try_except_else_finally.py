'''Contains examples about try-except-else-finally statement.'''


def divide(x: float, y: float) -> float:
    try:
        result = x / y
    except ZeroDivisionError:  # except ZeroDivisionError as err:
        print("Division by zero!")  # print(f"There was an error: {err}")
    else:
        print("Result is", result)
    finally:
        print("Executing finally clause.")


divide(2, 1)
# Result is 2.0
# Executing finally clause.

divide(2, 0)
# Division by zero!
# Executing finally clause.

divide("2", "1")
# Executing finally clause.
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#   File "<stdin>", line 4, in divide
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
