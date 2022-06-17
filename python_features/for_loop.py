
# Output:
# a
# b
# c
# Enters 'else' statement of 'for' loop.

def for_loop_executing_else_clause() -> None:
    letters_list = ['a', 'b', 'c']
    
    for letter in letters_list:
        print(letter)
    else:  # The 'else' clause applies to 'while' loop, too.
        print("Enters 'else' statement of 'for' loop.")


for_loop_executing_else_clause()
