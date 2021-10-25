def removeDuplicates(arr):
    newArr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] == arr[j]:
                    newArr.append(j)

    return newArr

print(removeDuplicates([1,2,3,4,5,5]))
