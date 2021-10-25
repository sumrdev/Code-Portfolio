class Car:
    def __init__(self, plate, engineType):
        self.plate = plate
        self.engineType = engineType
    
    def properties(self):
        print(type(self).__name__,"_____________________________")
        print("The numberplate is: ", self.plate) 
        print("This engine is: ", self.engineType)

class Tesla(Car):
    def __init__(self, plate, engineType, selfDriving, type):
        super().__init__(plate, engineType)
        self.selfDriving = selfDriving
        self.type = type
        if self.type == "s" or self.type == "S" or self.type == "X" or self.type == "x":
            self.horsePower = 1020
        elif self.type == "Y" or self.type == "y" or self.type == "3":
            self.horsePower = 490

    def properties(self):
        super().properties()
        if self.selfDriving: print("Self driving is available")
        else: print("Self driving is not available")
        print("Model ", self.type )
        print("This car has ", self.horsePower, " horsepower.")
        print("__________________________________")
        print(" ")

class Volvo(Car):
    def __init__(self, plate, engineType, os):
        super().__init__(plate, engineType)
        self.os = os
    
    def properties(self):
        super().properties()
        print("Operating system: ", self.os)
        print("__________________________________")
        print(" ")

class Audi(Car):
    def __init__(self, plate, engineType, shape):
        super().__init__(plate, engineType)
        self.shape = shape

    def properties(self):
        super().properties()
        print("Car type: ", self.shape)
        print("__________________________________")
        print(" ")

car = []
car.append(Tesla("CS30033", "Electric", True, "S"))
car.append(Volvo("SES BRO", "Electric", "Google"))
car.append(Audi("FARSDYT","Gas","Sedan"))
for i in car:
    i.properties()

