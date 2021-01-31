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