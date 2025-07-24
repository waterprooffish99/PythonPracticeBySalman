from abc import ABC, abstractmethod

# Abstract base class
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

# Another class for hobbies
class Hobby:
    def __init__(self, hobby):
        self.hobby = hobby

    def show_hobby(self):
        print(f"{self.hobby} is my favorite hobby.")

# Class that uses multiple inheritance
class TeacherWithHobby(Person, Hobby):
    def __init__(self, name, hobby):
        Person.__init__(self, name)
        Hobby.__init__(self, hobby)

    def work(self):
        print(f"{self.name} teaches students.")

# Create object
teacher = TeacherWithHobby("Ali", "Painting")

# Call methods from both parent classes
teacher.work()         # From Person
teacher.show_hobby()   # From Hobby
