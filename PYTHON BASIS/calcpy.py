import math
from decimal import *
getcontext().prec = 300

def calculatePi(k):
    calculations = 12
    a = (426880*math.sqrt(10005))
    
    pi = 0
    for i in range(calculations):
        currentK = math.factorial(6*k)*(545140134*k+13591409)/(math.factorial(3*k)*math.pow(math.factorial(k),3)*math.pow(-262537412640768000,k))
        pi = pi + currentK
        k =+ 1
    
    return a/pi

print(calculatePi(0, 100))
print("3,1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")