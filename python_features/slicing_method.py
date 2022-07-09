
# - In Python, a Sequence can be treated as order or unorder. A Sequence is called an Order Sequence if it allows indexing.
# Something allows indexing if and only if it allows slicing.
# Example of Order Sequence are str, range, tuple, list.

# - A Sequence is called an Unorder Sequence if it does NOT allow indexing. So, it also does NOT allow slicing.
# Example of Unorder Sequence (neither indexing nor slicing) are set, frozenset, dict.

letters = "abcdef"
print("letters =", letters)  # "abcdef"
print()

print("letters[3:5] =", letters[3:5])  # "de"
print("letters[0:len(letters)] =", letters[0:len(letters)])  # "abcdef"
print("letters[:] =", letters[:])  # "abcdef" because it is equivalent to letters[0:len(letters)]
print("letters[0:] =", letters[0:])  # "abcdef" because it is equivalent to letters[0:len(letters)]
print("letters[:5] =", letters[:5])  # "abcde" because it is equivalent to letters[0:5]
print("letters[0:5:2] =", letters[0:5:2])  # "ace"
print()
