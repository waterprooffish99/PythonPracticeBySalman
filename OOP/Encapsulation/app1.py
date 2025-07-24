class Car:
    def __init__(self):
        self.__speed = 0  # 🔒 private variable

    def set_speed(self, value):
        if 0 <= value <= 200:
            self.__speed = value
        else:
            print("Speed must be between 0 and 200")

    def get_speed(self):
        return self.__speed

    def increase_speed(self, amount):
        if self.__speed + amount <= 200:
            self.__speed += amount
        else:
            print("Cannot go over 200 speed!")

    def decrease_speed(self, amount):
        if self.__speed - amount >= 0:
            self.__speed -= amount
        else:
            print("Speed cannot go below 0")
