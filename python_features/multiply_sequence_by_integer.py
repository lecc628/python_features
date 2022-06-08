
# Output:
# seasons: ['Spring', 'Summer', 'Fall', 'Winter']
# seasons * 3: ['Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter']
# Change to new string object the second element in the sequence: ['Spring', 'aaaa', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer', 'Fall', 'Winter']

# list_of_ClassWithIntegerField: [11, 22, 33]
# list_of_ClassWithIntegerField * 3: [11, 22, 33, 11, 22, 33, 11, 22, 33]
# Change to new ClassWithIntegerField(44) object the second element in the sequence: [11, 44, 33, 11, 22, 33, 11, 22, 33]
# Change to new 55 value the integer value of the ClassWithIntegerField object of the first element in the sequence: [55, 44, 33, 55, 22, 33, 55, 22, 33]

class ClassWithIntegerField:
    def __init__(self, value: int) -> None: 
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

def multiply_sequence_by_integer() -> None:
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print("seasons: {}".format(seasons))

    seasons = seasons * 3
    print("seasons * 3: {}".format(seasons))

    seasons[1] = "aaaa"
    print("Change to new string object the second element in the sequence: {}".format(seasons))

    print()

    #vowels = [['a', 'e', 'i', 'o', 'u']]
    #print("vowels: {}".format(vowels))

    #vowels = vowels * 3
    #print("vowels * 3: {}".format(vowels))

    #vowels[1] = ['word']
    #print("modify the second value: {}".format(vowels))

    list_of_ClassWithIntegerField = [ClassWithIntegerField(11), ClassWithIntegerField(22), ClassWithIntegerField(33)]
    print("list_of_ClassWithIntegerField: {}".format(list_of_ClassWithIntegerField))

    list_of_ClassWithIntegerField = list_of_ClassWithIntegerField * 3
    print("list_of_ClassWithIntegerField * 3: {}".format(list_of_ClassWithIntegerField))

    list_of_ClassWithIntegerField[1] = ClassWithIntegerField(44)
    print("Change to new ClassWithIntegerField(44) object the second element in the sequence: {}".format(list_of_ClassWithIntegerField))
 
    list_of_ClassWithIntegerField[0].value = 55
    print("Change to new 55 value the integer value of the ClassWithIntegerField object of the first element in the sequence: {}".format(list_of_ClassWithIntegerField))

multiply_sequence_by_integer()
