def mergelists(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] <= l2[j] and l1[i+1] >= l2[j]:
                l1.insert(i,l2[j])
                l2.pop(j)
    print(l1)
mergelists([1,2,4],[1,3,4])