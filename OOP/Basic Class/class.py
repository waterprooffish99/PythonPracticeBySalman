# #basic class...

# class Student:
#     name = "ratan lal"

# # Creating Objet(Instance)...

# s1 = Student()          # This is called Objetc Or Instance, both are same.
# print(s1)               # this will print <__main__.Student object at 0x0000027B75CCD310>
# print(s1.name)          #  this will print the student name ratal lal....

# s2 = Student()
# print(s2.name)          # this will print the same name because value is not changed.

# # Another Example,,,,

# class Car:
#     name = "corolla"            # We can pass as many parameters as we want.Like brand or color or more,,,
#     brand = "toyota"
#     color = "Black"

# car1 = Car()
# print(car1.name)
# print(car1.brand)
# print(car1.color)

# Another Basic Class...

class Dog:                                  # class is a blueprint or a design or map...
    def __init__(self, name, breed):        # Constructor Method
        self.name = name                    # Attributes.
        self.breed = breed

    def bark(self):                         #method
        print(f'{self.name} says Bhow Bhow!')


# Now creating Objects...
dog1 = Dog("tony", "german shapered")
dog2 = Dog("jimmy", "Labrador")
dog3 = Dog("Zardari", "PPP")
dog4 = Dog("shehbazsharif", "PMLN")

# Now Using attributes and Methods....
print(dog1.name)
print(dog1.breed)
(dog1.bark())
print (dog2.name)
print(dog2.breed)
print(dog3.name)
print(dog3.breed)
(dog3.bark())
print(dog4.name)
print(dog4.breed)
(dog4.bark())


# another class...
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return(f'Assalam O Alaikom! I am {self.name}, and I am {self.age} years old')

h1 = Human("Salman", 39)
h2 = Human("Zyesha", 7)
h3 = Human("NoorUlHuda", 3)


print(h1.name)
print(h1.age)
print(h1.speak())

print(h2.name)
print(h2.age)
(h3.speak())

print(h3.name)
print(h3.age)
(h3.speak())





#creating another besic class..
class Car:
    def __init__(self, name, make):
        self.name = name 
        self.make = make

    def starts(self):
        print(f"{self.name} starts! {self.make} makes sound very impressive.")

car1 = Car("Toyota", "Corrola")

print(car1.name)
print(car1.make)
car1.starts()


class Bird:
    def __init__(self, name, color):
        self.name = name 
        self.color = color

    def sing(self):
        return f"{self.name} sings very beautifully!"
    
    def fly(self):
        print(f"{self.name} with {self.color} is flying high in the sky!")
    
bird1 = Bird("Parrot" , "Blue with Yellow Head")

print(bird1.name)
print(bird1.color)


print(bird1.sing())
bird1.fly()


#another example....

class Fan:
    def __init__(self, brand, speed):
        self.brand = brand 
        self.speed = speed

    def turn_on(self):
        return f"{self.brand} fan is now ON at {self.speed} speed."
    
    def turn_off(self):
        print(f"{self.brand} is now OFF. Stay cool...!")

fan1 = Fan("Ac/Dc Pak Fan", "High")

print(fan1.brand)
print(fan1.speed)

print(fan1.turn_on())
fan1.turn_off()

fan2 = Fan("Ac/Dc Pak Fan", "Medium")

print(fan2.brand)
print(fan2.speed)

print(fan2.turn_on())
fan2.turn_off()

fan3 = Fan("Ac/Dc Pak Fan", "Low")

print(fan3.brand)
print(fan3.speed)

print(fan3.turn_on())
fan3.turn_off()