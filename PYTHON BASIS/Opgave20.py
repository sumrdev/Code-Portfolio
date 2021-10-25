from random import randint 

def genLotto():
    numbers = []
    for i in range(7): numbers.append(randint(1,40))
    numbers.sort()
    return str(numbers)

print("Din lotto kupon er: " + genLotto())