#
# exemplu   G = z4 x z10
#           x = (2, 2) 
#           ord(x) = ?
#

import util
from math import gcd, lcm 

z1 = int(input("primul z: "))
z2 = int(input("al doilea z: "))

x1 = int(input("primul x: "))
x2 = int(input("al doilea x: "))

print("-------------\n")

print(f"x = ({x1}, {x2}), ord(x) = ?\n")
print(f"ord(x) = [ord({x1}), ord({x2})]  unde [a, b] = cmmmc[a, b]\n")

print("Fie ū ∈ Zn, atunci ord(ū) = n/(n, ū)  unde (n, ū) = cmmdc(n, ū)\n")


ord1 = util.aflaOrdinText(z1, x1)
ord2 = util.aflaOrdinText(z2, x2)

if ord1 == 0 or ord2 == 0:
    exit(0)

print(f"=> ord(x) = cmmmc [{ord1}, {ord2}] = {lcm(ord1, ord2)}")