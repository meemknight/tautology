#
# exemplu   Det el de ordin 50 din Z25 x Z10
#

import util
from math import gcd, lcm 
import itertools

def ordineXY(z):

    print(f"ord(x(căciulă)) / |Z{z}| =>\nord(x(căciulă)) / {z} => ")

    print("ord(x(căciulă)) ∈ { ", end='')

    ret = []

    separator = ''
    for i in range(1,z+1):
        if z % i == 0:
            print(f"{separator}{i}", end='')
            ret.append(i)
            separator = ", "
    print(" }")
    return ret

ordin = int(input("Ordinul: "))
z1 = int(input("Z1 : "))
z2 = int(input("Z2 : "))

#ordin = 50
#z1 = 25
#z2 = 10

cardinal = z1 * z2

print(f"G = (Z{z1}, Z{z2})")
print(f"Cardinal G = {z1} * {z2} = {cardinal}")

print(f"trebuie ca {ordin} / |G| ")

if( cardinal % ordin != 0):
    print("fals")
    exit(0)

print("adevărat\n")

print(f"fie (x(căciula), y(altă căciulă)) ∈ G cu ord(x, y) = {ordin} <=> [ord(x), ord(y)] = {ordin},   unde [a, b] = cmmmc(a, b)\n")

ordX = ordineXY(z1)
print()
ordY = ordineXY(z2)

products = itertools.product(ordX, ordY)

for x, y in products:
    if lcm(x, y) == ordin:
        print("\n\n Pentru:")
        print(f"ord(x) = {x}")
        print(f"ord(y) = {y}\n")
        util.rezolvareElDeOrdin(x, z1, 'x')
        util.rezolvareElDeOrdin(y, z2, 'y')
        

print("")