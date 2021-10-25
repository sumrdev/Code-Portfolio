def sumAll(arr):
    sumArr = 0
    for i in range(len(arr)):
        sumArr = sumArr + arr[i]
    return sumArr
print(sumAll([1,2,3]))