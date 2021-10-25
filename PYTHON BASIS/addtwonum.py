def addTwoNUm(l1,l2):
    a = ""
    b = ""
    for i in range(len(l1)):
        a += str(l1[i])
    for i in range(len(l2)):
        b += str(l2[i])
    a = int(a)
    b = int(b)
    return str(a+b)[::-1]
print(addTwoNUm([2,4,3],[5,6,4]))