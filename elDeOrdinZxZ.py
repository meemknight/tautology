#
# exemplu   Det el de ordin 50 din Z25 x Z10
#


import util
from math import gcd, lcm 
from elDeOrdin import rezolvareElDeOrdin

#ordin = int(input("Ordinul: "))
#z1 = int(input("Z1 : "))
#z2 = int(input("Z2 : "))

ordin = 50
z1 = 25
z2 = 10

cardinal = z1 * z2

print(f"G = (Z{z1}, Z{z2})")
print(f"Cardinal G = {z1} * {z2} = {cardinal}")

print(f"trebuie ca {ordin} / |G| ")

if( cardinal % ordin != 0):
    print("fals")
    exit(0)

print("adevărat\n")

print(f"fie (x(căciula), y(altă căciulă)) ∈ G cu ord(x, y) = {ordin} <=> [ord(x), ord(y)] = {ordin},   unde [a, b] = cmmmc(a, b)")

#ord1 = rezolvareElDeOrdin(ordin, z1)
#ord2 = rezolvareElDeOrdin(ordin, z2)

print("")