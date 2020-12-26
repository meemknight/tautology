#
# exemplu   Det el de ordin 12 din Z180
#

import util
from math import gcd, lcm 

ordin = int(input("Ordinul: "))
z = int(input("Z cât: "))

print("\n\n---------------------")

print(f"Determinați elementul de ordin {ordin} din Z {z}\n")

print("Fie ū ∈ Zn, atunci ord(ū) = n/(n, ū)  unde (n, ū) = cmmdc(n, ū)\n")
print(f"=> fie x ∈ Z{z}\n=> {ordin} = {z}/({z}, x) \n=> {ordin}*({z}, x) = {z}")

if z%ordin != 0:
    print(f"Ordinul trebuie să fie submultiplu de {z}, iar {ordin} nu este submultiplu de {z}\n=> Nu există elemente de ordin {ordin} din Z{z}\n")
    exit(0)

div = z // ordin

print(f"=> ({z}, x) = {div}\n")

util.descompunereText(z)
util.descompunereText(div)

print(f"=> {div}(căciulă) / x ")

factoriZ = util.descompunere(z)
factoriDiv = util.descompunere(div)

if z % div != 0:
    print(f"Ecuația nu are soluții\n=> Nu există elemente de ordin {ordin} din Z{z}\n")
    exit(0)

for key, val in factoriZ.items():
    if val == 0:
        continue
    
    if key not in factoriDiv:
        print(f"{key}(căciulă) nu divide x")
    elif factoriDiv[key] == val:
        pass
    else:
        for i in range(factoriDiv[key]+1, factoriZ[key]+1):
            print(f"{pow(key, i)}(căciulă) nu divide x")

print("")

rez = []

for i in range(1,  z):
    if(gcd(z,i) == div):
        rez.append(i)


print("=> x = ( ", end = '')
separator = ''
for i in rez:
    print(separator, end='')
    print(f"{i}", end='')
    separator = '; '

print(') (căciuli)')