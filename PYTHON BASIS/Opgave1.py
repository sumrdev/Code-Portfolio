import math
subject = "Sukkertoppen Gymnasium er et stort veldrevet gymnasium med en stærk profil inden for naturvidenskab, teknologi og design. Hos os er et højt fagligt niveau og godt socialt miljø nøglebegreber, og vi sætter elevinddragelse højt."
s = 1
p = 0
lw = 0
nw = 0

def lix():
    global nw, s, p, lw
    for i in subject:
        if i == " ":
            s+=1
        if i ==".":
            p +=1
        if i !=" ":
            nw +=1
        elif i==" ":
            if nw >= 7:
                lw +=1
            nw = 0

    return math.floor((s/p)+(lw*100)/s)

def lixDifficulty():
    lixn = lix()
    if lixn < 25:
        return str(lixn) + " | Let tekst for alle læsere, f.eks. børnelitteratur."
    if 25 <= lixn < 25:
        return str(lixn) + " | Let for øvede læsere, f.eks. ugebladslitteratur og skønlitteratur for voksne."
    if 35 <= lixn < 45:
        return str(lixn) + " | Middel, f.eks. dagblade og tidsskrifter."
    if 45 <= lixn < 55:
        return str(lixn) + " | Svær, f.eks. saglige bøger, populærvidenskabelige værker, akademiske udgivelser."
    if lixn >= 55:
        return str(lixn) + " | Meget svær, faglitteratur på akademisk niveau, lovtekster."

print(lixDifficulty())