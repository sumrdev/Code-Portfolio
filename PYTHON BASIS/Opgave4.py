def opg(n):
    if n**2 < 12000: n +=1; return opg(n) 
    else: return n
print(opg(1))