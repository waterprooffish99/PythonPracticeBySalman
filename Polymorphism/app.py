"""🔵 What is Polymorphism?
Poly means “many”
Morph means “forms”

✅ Polymorphism means: same function name, but different behaviors in different classes."""

class Dog():
    def speak(self):
        print("Woof!")

class Cat():
    def speak(self):
        print("Meow!")

def pet_speak(pet):
    pet.speak()

dog = Dog()
cat = Cat()

pet_speak(dog)
pet_speak(cat)
