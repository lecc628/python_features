'''Contains examples about slicing method.'''


# - In Python, a Sequence can be treated as order or unorder. A Sequence is
# called an Order Sequence if it allows indexing.
# Something allows indexing if and only if it allows slicing.
# Example of Order Sequence are str, range, tuple, list.
#
# - A Sequence is called an Unorder Sequence if it does NOT allow indexing.
# So, it also does NOT allow slicing.
# Example of Unorder Sequence (neither indexing nor slicing) are set,
# frozenset, dict.
#
# - s[:: step] is equivalent to:
#   s[0 : len(s) : step] if and only if step > 0
#   s[-1 : -len(s)-1 : step] if and only if step < 0

LETTERS = "abcdef"
print("LETTERS =", LETTERS)  # "abcdef"
print()

print("LETTERS[3:5] =", LETTERS[3:5])  # "de"
print("LETTERS[0:len(LETTERS)] =", LETTERS[0:len(LETTERS)])  # "abcdef"
print("LETTERS[:] =", LETTERS[:])  # "abcdef" because it is equivalent to LETTERS[0:len(LETTERS)]
print("LETTERS[::1] =", LETTERS[::1])  # "abcdef" because step = 1 > 0, then it is equivalent to LETTERS[0:len(LETTERS):1]
print("LETTERS[0:] =", LETTERS[0:])  # "abcdef" because it is equivalent to LETTERS[0:len(LETTERS)]
print("LETTERS[:5] =", LETTERS[:5])  # "abcde" because it is equivalent to LETTERS[0:5]
print("LETTERS[0:5:2] =", LETTERS[0:5:2])  # "ace"
print()

print("LETTERS[-3:5] =", LETTERS[-3:5])  # "de" because it is equivalent to LETTERS[-3:5:1]
print("LETTERS[-3:-5] =", LETTERS[-3:-5])  # "" because it is equivalent to LETTERS[-3:-5:1]
print("LETTERS[-3:-5:-1] =", LETTERS[-3:-5:-1])  # "dc"
print("LETTERS[-3:-6:-1] =", LETTERS[-3:-6:-1])  # "dcb"
print("LETTERS[-1:-len(LETTERS)-1:-1] =", LETTERS[-1:-len(LETTERS)-1:-1])  # "fedcba"
print("LETTERS[::-1] =", LETTERS[::-1])  # "fedcba" because step = -1 < 0, then it is equivalent to LETTERS[-1:-len(LETTERS)-1:-1]
print("LETTERS[:3:-1] =", LETTERS[:3:-1])  # "fe" because it is equivalent to LETTERS[-1:3:-1]
print("LETTERS[:1:-1] =", LETTERS[:1:-1])  # "fedc" because it is equivalent to LETTERS[-1:1:-1]
print("LETTERS[2::-1] =", LETTERS[2::-1])  # "cba" because it is equivalent to LETTERS[2 : -len(LETTERS)-1 : -1]
print()
