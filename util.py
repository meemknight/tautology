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