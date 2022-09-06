'''Contains examples about iterable packing and unpacking.'''


# In function parameters:
# When you use *args and **kwargs, they have the tuple and dict
# types respectively.
#
# In iterable unpacking:
# When you use *values, it has the list type.

from typing import Any, List

px: float = 1.0
py: float = 2.0
pz: float = 3.0

name: str = "Luis Enrique"
phone: str = "+34 123 45 67 89"
# It can be any iterable form (tuple, list, dict, etc.).
rest: List[Any] = ["email@gmail.com", "Address 1", "Address 2"]

# Iterable packing (regular or extended forms):
#
# regular form
pos = px, py, pz
# extended form
info = name, phone, *rest

print(pos)
print(info)
print()

# Iterable unpacking (regular or extended forms):
#
# regular form
var_px, var_py, var_pz = pos
# extended form (the type of var_rest is list).
var_name, var_phone, *var_rest = info

print(var_px, var_py, var_pz, var_name, var_phone, var_rest, sep="\n")
