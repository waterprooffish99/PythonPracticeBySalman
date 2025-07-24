# parent class...
class Vehicle:
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} vehicle is starting..."

# Child Class...   
class Car(Vehicle):
    def start(self):          # Overriding the start method.
        return f"{self.brand} car goes VVVrooooommmmmmmmm!"
    

v = Vehicle("Generic")
c = Car("Mazda")

print(v.start())
print(c.start())