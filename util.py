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
    return factori

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

        
def rezolvareElDeOrdin(ordin, z, necunoscuta = 'x'):

    print("\nFie ū ∈ Zn, atunci ord(ū) = n/(n, ū)  unde (n, ū) = cmmdc(n, ū)\n")
    print(f"=> fie {necunoscuta} ∈ Z{z}\n=> {ordin} = {z}/({z}, {necunoscuta}) \n=> {ordin}*({z}, {necunoscuta }) = {z}")

    if z%ordin != 0:
        print(f"Ordinul trebuie să fie submultiplu de {z}, iar {ordin} nu este submultiplu de {z}\n=> Nu există elemente de ordin {ordin} din Z{z}\n")
        return []

    div = z // ordin

    print(f"=> ({z}, {necunoscuta}) = {div}\n")

    descompunereText(z)
    descompunereText(div)

    print(f"=> {div}(căciulă) / {necunoscuta} ")

    factoriZ = descompunere(z)
    factoriDiv = descompunere(div)

    if z % div != 0:
        print(f"Ecuația nu are soluții\n=> Nu există elemente de ordin {ordin} din Z{z}\n")
        return []

    for key, val in factoriZ.items():
        if val == 0:
            continue
        
        if key not in factoriDiv:
            print(f"{key}(căciulă) nu divide {necunoscuta }")
        elif factoriDiv[key] == val:
            pass
        else:
            for i in range(factoriDiv[key]+1, factoriZ[key]+1):
                print(f"{pow(key, i)}(căciulă) nu divide {necunoscuta }")

    print("")

    rez = []

    for i in range(1,  z):
        if(gcd(z,i) == div):
            rez.append(i)

    print(f"=> {necunoscuta} = ( ", end = '')
    separator = ''
    for i in rez:
        print(separator, end='')
        print(f"{i}", end='')
        separator = '; '

    print(') (căciuli)')

    return rez


