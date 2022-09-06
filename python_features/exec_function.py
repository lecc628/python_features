'''Contains examples about exec function.'''


# Simple use of exec() function.

PROGRAMME_1 = 'a = 5\nb = 10\nprint("Sum =", a + b)'
exec(PROGRAMME_1)  # Sum = 15

print("\n/***************************************************************/\n")

# exec() with a single line programme input.
# Gets a single line programme as input.
programme_2 = input('Enter a programme: ')

# Write [print(item) for item in [1, 2, 3]]
exec(programme_2)  # Executes the programme.
