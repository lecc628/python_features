
# Output:
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# enumerate(seasons) = <enumerate object at memory_address>
# list(enumerate(seasons)) = [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

def enumerate_function() -> None:
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(f"{seasons = }")
    print(f"{enumerate(seasons) = }")
    print(f"{list(enumerate(seasons)) = }")

enumerate_function()
