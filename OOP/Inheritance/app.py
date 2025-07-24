class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound!"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):  # Override the parent's speak method
        return f"{self.name} says Woof!"

#Creating Objects...
generic_animal = Animal("Creature")
dog = Dog("Buddy")

print(generic_animal.speak())
print(dog.speak())