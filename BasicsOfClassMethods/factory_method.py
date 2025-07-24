"""2. Factory Methods

Class methods can be used as factory methods 
to create instances in a more controlled manner."""

#  Example 1: Creating Object Using Class Method (Factory Method).

class Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, student_str):
            name = student_str
            return cls(name)
        
# Create object using class method..,

s1 = Student.from_string("Salman")
print(s1.name)