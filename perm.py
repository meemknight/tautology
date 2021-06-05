import math

def nextEl(perm, el):
    return perm[el-1]



permutare = [int(i) for i in input().split()]
lungime = len(permutare)

valid = True

for i in range(1, lungime + 1):
    if i not in permutare:
        valid = False
        break

if not valid:
    print("permutare not valida\n")
    exit(0)


print("\n\nσ = ", permutare)


print("\na)Descompuneți permutarea σ în produs de cicli disjuncți:")
copie = permutare.copy()

cicli = []

while len(copie) > 0:
    element = copie[0]
    copie = copie[1:]

    elCiclu = []
    elCiclu.append(element) 

    while True:
        element = nextEl(permutare, element)
        if element != elCiclu[0]:
            elCiclu.append(element) 
            copie.remove(element)
        else:
            break

    if len(elCiclu) > 1:
        elCiclu = [elCiclu[-1]] + elCiclu[:-1]
        print(elCiclu, end=' ')    
        cicli.append(elCiclu)


print("\n\nb)Descompuneți permutarea σ în produs de transpozitii:")

transpozitii = []

for i in cicli:
    j = 0
    while j < len(i)-1:
        transpozitii.append((i[j], i[j+1]))
        j += 1

print(transpozitii)

signatura = (-1)**len(transpozitii)

print("\nc)Determinați signatura permutarii σ:  ( ε(σ) )")
print(f"Avem N={len(transpozitii)} transpoziții în descompunerea lui σ")
print(f"ε(σ) = (-1)^N = (-1)^{len(transpozitii)} = {signatura}")

print("\nd)Determinați tipul permutarii σ: (pară/impară)")
print(f"Cum ε(σ) = {signatura} => σ este permutare {'pară' if signatura == 1 else 'impară'}")

print("\ne)Determinați σ^-1: (procedeu: se scrie permutarea de sus in jos)")
permutareInversa = []

for i in range(1, lungime+1):
        for j in range(0, lungime):
            if(permutare[j] == i):
                permutareInversa.append(j+1)

print(permutareInversa)

print("\nf)Determinați σ^2:")
permutarePatrat = []
for i in range(1, lungime+1):
    permutarePatrat.append(nextEl(permutare, nextEl(permutare, i) ))
    
print(permutarePatrat)

print("\nf)Determinați ordinul σ:    (la ce putere e permutare identica)")
print("ordinul unei permutări este cmmmc[ordin cicli]")
print("ordinul unui ciclu este lungimea ciclului =>")
lungimiCicli = [len(i) for i in cicli]
ordin = math.lcm(*lungimiCicli)
print(f"ord(σ) = [{lungimiCicli}] = {ordin}")


print("\ng)Determinați ordinul x^2 = σ:")
if signatura == 1:
    print("Programul nu stie sa rezolve asta :(((")
else:
    print("x^2 permutare pară")
    print("σ este impară (aflat la d) => ecuația nu are soluții.")


#print("\nh)Determinați ordinul x^3 = σ:")



print("\n)Determinați ordinul σ^x:")
x = int(input("introdu x: "))
print(f"ordin(σ^{x}) = ordin(σ)/(ordin(σ), {x}) = {ordin}/({ordin}, {x}) = {ordin}/{math.gcd(ordin, x)} = {ordin / math.gcd(ordin, x)} ")
