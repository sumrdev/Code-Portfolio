#1 Animal er parent class
#age er en integer
#Gender er en string
#boolean er en variabel der kan være sandt eller falsk
#mate() er en funktion


class Animal():
    def __init__(self, food, age, gender):
        self.lastFed = food
        self.age = age
        self.gender = gender
    
    def isMammal(self, stat):
        if not stat: return False
        elif stat: return True
    
    def mate(self, animal):
        if type(self) == type(animal) and self.gender != animal.gender: return "Mating Success"
        if type(self) != type(animal) or self.gender == animal.gender: return "Incompatible"
        else: print(animal)


class Duck(Animal):

    def __init__(self, food, age, gender, beakColor, swimStat):
        self.beak = beakColor
        self.swimStat = swimStat
        self.mammal = True
        Animal.isMammal(self, self.mammal)
        super().__init__(food,age,gender)

    def swim(self):
        if self.swimStat: print("The Duck is swimming"); return True
        elif not self.swimStat: print("The Duck is not swimming"); return False


class Fish(Animal):

    def __init__(self,food,age,gender, sizeInFt, eatStat, swimStat):
        self.sizeInFt = sizeInFt
        self.eatStat = eatStat
        self.swimStat = swimStat
        self.mammal = False
        Animal.isMammal(self, self.mammal)
        super().__init__(food,age,gender)
    
    def swim(self):
        if self.swimStat: print("The Fish is swimming"); return True
        elif not self.swimStat: print("The Fish is not swimming"); return False

class Zebra(Animal):

    def __init__(self, food, age, gender, wildStat, runStat):
        self.wild = wildStat
        self.runStat = runStat
        self.mammal = True
        Animal.isMammal(self, self.mammal)
        super().__init__(food,age,gender)     
    def run(self):
        if self.runStat: print("The Zebra is running"); return True
        elif not self.runStat: print("The Zebra is not running"); return False

class Monkey(Animal):
    def __init__(self, food, age, gender, color, foodType):
        self.color = color
        self.foodType = foodType
        super().__init__(food,age,gender)

class Gorilla(Monkey):
    def __init__(self, food, age, gender, color, foodType, agressive):
        self.agressive = agressive
        super().__init__(food,age,gender,color,foodType)
        
    def agro(self):
        if self.agressive: print("The Gorilla is agressive!"); return True
        elif not self.agressive: print("The Gorilla is not agressive!"); return False

class Orangutang(Monkey):
    def __init__(self, food, age, gender, color, foodType, agressive):
        self.agressive = agressive
        super().__init__(food,age,gender,color,foodType)
        
    def agro(self):
        if self.agressive: print("The Orangutang is agressive!"); return True
        elif not self.agressive: print("The Orangutang is not agressive!"); return False

