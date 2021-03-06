from util import *
from math import gcd
from functools import reduce
import itertools

z = int(input("Z cât: "))

print("\n---------------")
print("a) Găsiți el. inversabile:")
print("În Zn, x̂ e inversabil <=>  (x, n) = 1")
print(r"Deci U(Zn) = {x̂  ∈ Z", z, r"/ (x,", z, r") = 1 }")

print(f"U(Z{z}) = ", r"{", sep='', end='')

rasp = []
for i in range(0, z):
    if gcd(i, z) == 1:
        rasp.append(i)

print(*rasp, sep=', ', end='}\n')
print(len(rasp))

print("")

print("b) Găsiți elementele nilpotente")
print("x e nilpotent <=> ∃ n ∈ N a.î. x^n = 0")
print("În Zn, x̂ e nilpotent <=> x conține toți factorii primi din descompunerea lui n.\n")

desc = descompunereText(z)

produsFactori = reduce(lambda x, y: x*y, desc.keys())

rez = []
for i in desc.keys():
    rez.append(i)

print(*rez, sep=' * ', end='')

print(f" = {produsFactori}")

print(f"=> {produsFactori}(căciulă) * Z{z} =", "{ ", end='')

i = produsFactori

nilpotenti = [0]
while i < z:
    nilpotenti.append(i)
    i += produsFactori
del i

print(*nilpotenti, sep=', ', end='}\n\n')

print("c) Găsiți divizorii lui zero")
print("x dacă ∃ x' a.î. x*x' = 0")
print(f"În Z{z} toate elementele x̂, (x, n) ≠ 1 sunt divizori ai lui 0 \n")

print( r"=> {", sep='', end='')

rasp = []
for i in range(1, z):
    if gcd(i, z) != 1:
        rasp.append(i)

print(*rasp, sep=', ', end='}\n\n')

print("d) Găsiți elementele idempotente.")
print("X e idempotent <=> x^2 = x\n")
print(f"Avem izomorfismul ρ: Z{z} -> ", end='')

rasp = []
izomorfism = []
for i in desc.keys():
    rasp.append("Z" + str(i ** desc[i]))
    izomorfism.append(i ** desc[i])

print( *rasp, sep=' x ')
print("ρ(a) = (", sep='', end='')
rasp = ['a'] * len(izomorfism)
print(*rasp, sep=', ', end=')    (fiecare a are altă căciulă)\n')
print("Cazul I : P^k / x <=> x ≡ 0(mod p^k) <=> x̂ = 0 (căciulă)")
print("Cazul II : P^k / x-1 <=> x-1 ≡ 0(mod p^k) <=> x̂-1 = 0 <=> x̂-1 = 0 <=> x̂ = 1 (căciuli peste toate numerele) ")
print("Deci singurii idempotenți din Z indice p, k sunt 0, 1 (căciuli)")
print(f"Așadar, idempotenții din z{z} sunt: \n")

it = itertools.product ([0,1],  repeat= len(izomorfism) )

for i in it:
    value = 0

    for j in range(0, z):
        k = 0
        good = True
        while k < len(izomorfism):
            if i[k] == 0:
                if j % izomorfism[k] != 0:
                    good = False
                    break
            else:
                if j % izomorfism[k] != 1:
                    good = False
                    break            
            k += 1

        if good:
            value = j
            break


    print(value, "<-", i, end=" ")
    print(" Acele elemente care: ")
    k = 0
    while k < len(izomorfism):

        if i[k] == 0:
            print(f"dau restul 0 la împărțirea cu {izomorfism[k]}" , end='\n')
        else:
            print(f"dau restul 1 la împărțirea cu {izomorfism[k]}" , end='\n')
        k += 1  
    print("")


print(f"e) Să se dea exemplu de polinoame nilpotente: ")
print(f"Un polinom este nilpotent dacă are coeficienții nilpotenți\n")

print(f"f) Să se dea exemplu de polinom inversabil: ")
print(f"Un polinom este inversabil dacă termenul liber e inversabil iar restul coeficienților sunt nilpotenți\n")

print(f"g) Să se determine elementele idempotente de grad cel mult ... din Z{z}[x]")
print(f"Se știe că polinoamele idempotente R[x] sunt constantele idempotente, așadar trebuie să determinăm\
elementele idempotente din Z{z}")
print(f"Aceiași Rezolvare de la punctul d).\n")


grad = int(input(f"h) Determinați numărul elementelor inversabile de grad cel mult: "))
print(f"din Z{z}[x]\n")
print(f"Știm că un polinom din R[x] este inversabil <=> are termenul liber inversabil, iar toți ceilalți \
coeficienți sunt nilpotenți")

subscript = ["₀" , "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]

print("Fie f = ", end='')

elements = []
for i in range(0, grad + 1):
    elements.append("a" + subscript[i] + "x^" + f"{i}")

print(*elements, sep = " + ", end=f" ∈ Z{z} inversabile.\n")
print(f"=> a₀ ∈ U(Z{z}), iar aₖ ∈ N(Z{z}), k ∈ ", end='')

elements = [i for i in range(1, grad+1)]
print("{ ", end='')
print(*elements, end=' }\n\n', sep=", ")
print(f"|U(Z{z})| = {z} * Produs (1-1/p) pentru p factor prim al lui {z}")
elements = [f"(1 - 1/{i})" for i in desc.keys()]
print(f"={z}", *elements,sep='')
elements = [1 - 1/i for i in desc.keys()]
produsFactori2 = reduce(lambda x, y: x*y,elements)
print(f"= {z * produsFactori2:.2f}\n")

elements = [i for i in range(1, grad+1)]
print("|N(Z{z})| = | ", end='')
print(*elements, sep=" * ", end='')
print(f" (căciulă) Z{z}| = {len(nilpotenti)}")
print(f"Deci, numărul elementelor inversabile de grad cel mult {grad} din Z{z}[x] este: \
   {z * produsFactori2 :.2f} * {len(nilpotenti)} ^ {grad}  = {z * produsFactori2 * (len(nilpotenti) ** grad) :.2f} ")