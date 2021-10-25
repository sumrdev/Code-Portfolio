def bubbleSort(arr):
    for i in range(len(arr)):
        if(arr[i] > arr[i+1]):
            h = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = h
            i -=2
    return arr

print(bubbleSort([2,4,3,6,1]))