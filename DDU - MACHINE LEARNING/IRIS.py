from sklearn.datasets import load_iris

from knnMNIST import decision
iris = load_iris()
iris.data[:,0]

k = 3

def decider(n1,n2):
    d = closer()

def tester(t):
    for i in range(2,t):
        result = decision(1,i)
        print(result, iris.target[i])
