from collections import defaultdict
from math import gcd, lcm 

def descompunere(x):
    if x == 0:
        return {0 : 1}
    
    if x == 1:
        return {1 : 1}

    rez = defaultdict(lambda: 0)

    i = 2
    while x > 1:
        if(x % i == 0):
            x//=i
            rez[i]+=1
        else:
            i+=1

    return rez

def descompunereText(x):
    print(f"Descompumere {x}:")

    factori = descompunere(x)
    
    sep = ''
    for key, val in factori.items():
        print(sep, end = '')
        if(val != 1):
            print (f"{key}^{val}", end = '')
        else:
            print (f"{key}", end = '')
        sep = ' * '

    print("\n")

def aflaOrdin(n, x):
    numitor = gcd(n, x)
    if n % numitor != 0:
        return 0
    return n // numitor

def aflaOrdinText(n, x):
    print(f"ord({x}) în Z{n} = {n} / ({n}, {2})")
    print(f"= {n} / {gcd(n, 2)}")
    ordin = aflaOrdin(n, x)

    if ordin == 0:
        print("Nu exista ordin\n")
        return 0
    else:
        print(f"= {ordin}\n")
        return ordin