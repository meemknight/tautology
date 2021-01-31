#
# exemplu   Det el de ordin 12 din Z180
#

import util
from math import gcd, lcm 

ordin = int(input("Ordinul: "))
z = int(input("Z : "))

print("\n\n---------------------")

print(f"Determinați elementul de ordin {ordin} din Z {z}  (grup cu adunare)\n")

util.rezolvareElDeOrdin(ordin, z)


print(f"\nDet ordinul unui element din Z{z}  (Zn cu adunarea)")
print(f"folosim formula ord(p) = n/(n, p) (cmmdc)   => ord(p) = {z}/({z}, p)")
for i in range(0, z):
    print(f"ord({i}) = {z} / {gcd(i, z) } = { z // gcd(i, z) } ")


print(f"\nDet ordinul unui element din Z{z}  (Zn cu înmulțirea)")
print("element^ordin = 1")
for i in range(1, z):
    ord = 1
    element = i
    while True:
        if element == 1:
            print(f"ordin {i} = {ord}\n")
            break
        else:
            print(f"{element} * {i} = {(element * i) % z}", end='=> ')
            element = (element * i) % z
            ord += 1
            if ord > z:
                print("elementul nu are ordin\n")
                break