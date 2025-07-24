class WaterBottle:
    def __init__(self):
        self.__water_level = 30

    def fill(self, amount):
        if amount > 0:
            self.__water_level += amount
        else:
            print("Invalid Amount")
    
    def get_level(self):
        return self.__water_level
    

bottle = WaterBottle()
bottle.fill(50)
print(bottle.get_level())