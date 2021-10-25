l1 = [1,2,4,5]
l2 = [1,3,4,6,7]

def mergeArray():
    i = 0
    while i < len(l1):
        print(len(l1))
        if(i == len(l1)):
            if(l1[i] <= l2[0] and l1[i+1] >= l2[0]):
                l1.insert(i+1,l2[0])
                l2.pop(0)
                i = 0
            elif(i == len(l1)):
                l1.append(l2[0])
                i = 0
        i+=1
    # print(l1)
    return l1

print(mergeArray())

#[1,1,2,3,4,4,5,6,7]