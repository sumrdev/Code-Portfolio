from Animals import *

fish = Fish(2,4,"male",2,True,False)
zebra = Zebra(3,10,"female",True,True)
duck = Duck(0,1, "male", "yellow", True)
gorilla = Gorilla(2,15,"male","blue","banana",True)
gorilla2 = Gorilla(3,14, "male", "green", "banana", False)
organgutang = Orangutang(3,20,"female", "orange", "children", True)

# print(fish.age)
# print(zebra.wild)
# print(duck.beak)
# fish.swim()
# duck.swim()
# gorilla.agro()
# organgutang.agro()
print(gorilla.gender)
print(gorilla2.gender)
print(gorilla.mate(gorilla2))