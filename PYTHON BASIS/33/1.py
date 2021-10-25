def largest(arr):
    l = 0
    for i in range(len(arr)):
        if arr[i] > l:
            l = arr[i]
    return l
print(largest([1,5,4,2,5,3,2,5,7,10,1]))