password = input("Type a password here: ")

def checkPassword(pw):
    pw = str(pw)
    length = True
    digits = True
    uppers = True
    lowers = True
    for i in range(len(pw)):
        if pw[i].isdigit() == True: digits = True
        if pw[i].isupper() == True: uppers = True
        if pw[i].islower() == True: lowers = True
        if pw[i]isSymbol()
    
    if len(pw) > 8 and digits and uppers and lowers: return "Strong Password"
    else: return "Weak Password"
    
print(checkPassword(password))