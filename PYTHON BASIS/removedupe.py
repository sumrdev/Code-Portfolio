def deletedupe(head):
    for i in range(len(head)-2):
        if head[i] == head[i+1]:
            head.pop(i+1)
            i-=2
    return head
print(deletedupe([1,1,2,3,4,4]))