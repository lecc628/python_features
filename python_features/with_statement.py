
# The with statement is used to wrap the execution of a code block with methods defined by a context manager.
#
#  - The protocol consisting of the __enter__() and __exit__() methods is known as the "context management protocol",
#  and the type that implements that protocol is known as "context manager".
#
#  - The type of the context expression should be a "context manager"; that is, a type that implements the "context management protocol".
#
#  - The with statement guarantees that if the __enter__() method returns without an error,
#  then __exit__() will always be called. Thus, if an error occurs during the assignment to
#  the target list, it will be treated the same as an error occurring within the suite would be.


# The execution of a with statement with one context expression proceeds as follows:
#
#  1. The context expression is evaluated to obtain a context manager.
#
#  2. The context manager's __enter__() is loaded for later use.
#
#  3. The context manager's __exit__() is loaded for later use.
#
#  4. The context manager's __enter__() is invoked.
#
#  5. If a target was included in the with statement, the return value from __enter__() is assigned to it.
#
#  6. The suite is executed.
#
#  7. The context manager’s __exit__() method is invoked. If an exception caused the suite to be exited,
#  its type, value, and traceback are passed as arguments to __exit__(). Otherwise, three None arguments
#  are supplied.
#
#  If the suite was exited due to an exception, and the return value from the __exit__() method was false,
#  the exception is reraised. If the return value was true, the exception is suppressed, and execution
#  continues with the statement following the with statement.
#
#  If the suite was exited for any reason other than an exception, the return value from __exit__() is ignored,
#  and execution proceeds at the normal location for the kind of exit that was taken.


# The following code:
#
# with EXPRESSION as TARGET:
#     SUITE
#
# is semantically equivalent to:
#
# from sys import exc_info
#
# manager = (EXPRESSION)
# enter = type(manager).__enter__
# exit = type(manager).__exit__
# value = enter(manager)
# hit_except = False
#
# try:
#     TARGET = value  # Only if "as TARGET" is present.
#     SUITE
# except:  # The exceptional case is handled here.
#     hit_except = True
#     if not exit(manager, *exc_info()):
#         raise
#     # The exception is swallowed if exit() returns true.
# finally:
#     if not hit_except:
#         exit(manager, None, None, None)


# With more than one context expression, the context managers are processed as if multiple with statements were nested:
#
# with A() as a, B() as b:
#     SUITE
#
# is semantically equivalent to:
#
# with A() as a:
#     with B() as b:
#         SUITE


# You can also write multi-item context managers in multiple lines if the items are surrounded by parentheses:
#
# with (
#     A() as a,
#     B() as b,
# ):
#     SUITE


# A generic "object-closing" context manager:

from typing import Any

class closing:
    def __init__(self, obj: Any) -> None:
        self.obj = obj

    def __enter__(self) -> Any:
        return self.obj

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        try:
            close_it = self.obj.close
        except AttributeError:
            pass
        else:
            close_it()
        finally:
            return False

# The closing type can be used to deterministically close anything with a close method, be it file, generator, or something else.
# It can even be used when the object isn’t guaranteed to require closing (e.g., a function that accepts an arbitrary iterable):
with closing(open("with_statement.py", "r")) as f:
    for line in f:
        print(line, end = "")

# Deterministically finalizes an iterator:
# with closing(iter(data_source)) as data:
#     for datum in data:
#         process(datum)
