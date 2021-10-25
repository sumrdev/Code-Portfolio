import math
import random
from collections import Counter
from mnist import MNIST
mndata = MNIST('./data')
mndata.gz = True
images, labels = mndata.load_training()

k = 13
print(images[0])


def euDist(img, img2):
    distance = math.sqrt(sum([(img[index] - img2[index]) ** 2 for index in range(len(img))]))
    return distance

def closer(image):
    
    closest = []
    for i in range(1,2000):
        closest.append([euDist(image,images[i]),labels[i]])
    closest.sort()
    return closest

def decision(image):
    d = closer(image)
    a = []
    for i in range(k):
        a.append(d[i][1])
        c = Counter(a)
    return c.most_common(1)[0][0]

def tester(testAmount):
    accuracy = 0
    for i in range(testAmount):
        rand = random.randint(0,1000)
        label = labels.pop(rand)
        result = decision(images.pop(rand))

        if result == label:
            print(" Guess: ", result,"Actual: ",label, "True!")
            accuracy +=1
        elif result != label:
            print(" Guess: ", result,"Actual: ", label, "False!")  
    print("Accuracy = ",(accuracy/testAmount)*100, "%")    
tester(100)
