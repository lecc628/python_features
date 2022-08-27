
# Simple use of exec() function.

programme_1 = 'a = 5\nb = 10\nprint("Sum =", a + b)'
exec(programme_1)  # Sum = 15

print("\n/*******************************************************************************************/\n")

# exec() with a single line programme input.
programme_2 = input('Enter a programme: ')  # Gets a single line programme as input.

# Write [print(item) for item in [1, 2, 3]]
exec(programme_2)  # Executes the programme.
