import random

def swappi(arr):
    runs = int((len(arr)-1)/2)
    if len(arr) > 1:
        if(len(arr) % 2 == 0):
            a = 0
        else:
            a = 1
        for i in range(runs):
            h = arr[i]
            print(h)
            arr[i] = arr[len(arr)-1-i]
            print(arr[i])
            arr[len(arr)-1-i] = h
            print(arr[len(arr)-1-i])
    return arr
print(swappi([1,2,3]))