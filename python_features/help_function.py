
class Student:
    '''Represents a student.'''

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

    def show(self) -> None:
        '''Shows the student name and age.'''
        print(f'{self.name = } {self.age = }')

# Shows help of Student class.
help(Student)
