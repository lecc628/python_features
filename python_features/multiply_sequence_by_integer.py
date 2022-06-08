
# Output:
# seasons: ['Spring', 'Summer', 'Fall', 'Winter']
# seasons * 3: ['Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter']
# Change to new string object the second element in the sequence: ['Spring', 'aaaa', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter']

def multiply_sequence_by_integer() -> None:
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print("seasons: {}".format(seasons))

    seasons = seasons * 3
    print("seasons * 3: {}".format(seasons))

    seasons[1] = "aaaa"
    print("Change to new string object the second element in the sequence: {}".format(seasons))

multiply_sequence_by_integer()
