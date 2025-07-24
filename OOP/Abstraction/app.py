# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False     # meaning we have not press any of them. not accelerator not break not clutch.

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started...!")

# car1 = Car()
# car1.start()

# Abstraction Haadi,,,

from abc import ABC , abstractmethod

# creating an abstract class...

class Animal(ABC):

    # Defining an abstract method,,,
    @abstractmethod
    def make_sound(self):
        pass


# Creating a child class....

class Dog(Animal):

    # implement the abstract method....
    def make_sound(self):
        print("Woof Woof!")

# Creating object calling the method...
dog = Dog()
dog.make_sound()


    

from abc import ABC , abstractmethod
class Shapes(ABC):

    @abstractmethod
    def area(self):
        pass

# Creating a Circle class,,,
class Circle(Shapes):
    def area(self):
        print("Area of circle = π × r × r")

# Creating a square class...
class Square(Shapes):
    def area(self):
        print("Area of square = side * side")

# Creating Object...
c = Circle()
c.area()

s = Square()
s.area()

from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Creating a Car class...
class Car(Vehicle):
    def start_engine(self):
        print("Car engine Started: Vrooooommmm!")

#Creating a Bike Class....
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started: brmmm brmmm!")

c = Car()
c.start_engine()

b = Bike()
b.start_engine()


from abc import ABC , abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class Meezan(ATM):
    def withdraw(self):
        print("Withdrawn from Meezan ATM!")

class Bank_Islami(ATM):
    def withdraw(self):
        print("Withdrawn from Bank Islami!")

m = Meezan()
m.withdraw()

bi = Bank_Islami()
bi.withdraw()


'''abstraction using super() function. 
super() is a built-in function in Python that is used to:

👉 Call a method from the parent class inside a child class.

It’s like saying:

“Hey Python, go to my abba (parent) and run their version of this method.”

🧠 Why use super()?
To reuse code from the parent class without rewriting it.'''

from abc import ABC , abstractmethod
class Animal(ABC):
    def sound(self):
        pass
    
    def intro(self):
        print("I am animal.")

class Dog(Animal):
    def sound(self):
        super().intro()     #calls parent class intro...
        print("Dog Says: Woof Woof!")


class Lion(Animal):
    def sound(self):
        super().intro() 
        print("Lion Says:Rooaaaarrrrrrr!")

class Cat(Animal):
    def sound(self):
        super().intro()
        print("Cat says: Meowwww!")

c = Cat()
c.sound()

l = Lion()
l.sound()

d = Dog()
d.sound()
