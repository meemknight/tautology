from copy import deepcopy
import itertools

def readClauza(c):
    negatie = c.startswith("!")
    simbol = c if not c.startswith("!") else c[1:]
    return (negatie, simbol)

def clauzaTriviala(c):
    for i in c:
        if readClauza(i)[0]:
            if i[1:] in c:
                return True
        else:
            if "!" + i  in c:
                return True
    
    return False

def clauzaPurTriviala(c):
    for i in c:
        if readClauza(i)[0]:
            if i[1:] in c:
                continue
        else:
            if "!" + i  in c:
                continue

        return False
    

def parseString(s):
    s = s.replace("{", "[")
    s = s.replace("}", "]")
    s = s.replace("¬", "!")
    s = s.replace("v", "")
    return s

def parsePrint(s):
    s = str(s)
    s = s.replace("[", "{")
    s = s.replace("]", "}")
    s = s.replace("!", "¬")
    #s = s.replace("", "")
    return s

#print(parseString(r"""{{¬v1, v2, ¬v4}, {¬v3, ¬v2}, {v1, v3}, {v1}, {v3}, {v4}}"""))

#s = [ ["1", "!3"], ["2", "1"], ["2", "!1", "3"]]
#s = [ ["!1", "2", "!4"], ["!3", "!2"], ["1", "3"], ["1"], ["3"], ["4"]]
#= {{¬v1, v2, ¬v4}, {¬v3, ¬v2}, {v1, v3}, {v1}, {v3}, {v4}}
s = [["!1", "2", "!4"], ["!3", "!2"], ["1", "3"], ["1"], ["3"], ["4"]]

I = 1
print(f"\ni := {I}, S1 := S.")


while True:
    x = input("Introdu variabila: ")


    tSimplu = []

    for i in s:
        if x in i:
            tSimplu += [i]
    
    tNegat = []
    
    for i in s:
        if "!" + x in i:
            tNegat += [i]

    #print(tSimplu)
    #print(tNegat, '\n')


    print(f"P{I}.1 x{I} := v{x};  ", sep="", end="")
    print(f"T¹{I} := {parsePrint(tSimplu)};  ", sep="", end="")
    print(f"T⁰{I} := {parsePrint(tNegat)};", sep="", end="")
    print("")
    
    "T¹ T⁰"

    tSimpluEliminat = deepcopy(tSimplu)    
    tNegatEliminat = deepcopy(tNegat)

    for i in tSimpluEliminat:
        if x in i:
            i.remove(x)

    for i in tNegatEliminat:
        if "!" + x in i:
            i.remove("!" + x)

    #print(tSimpluEliminat)
    #print(tNegatEliminat, "\n")

    u = []

    if tSimplu != [] and tNegat != []:
        for i in tSimpluEliminat:
            cur = i
            for j in tNegatEliminat:
                cur += j

            u+=[cur]

    
    print(f"P{I}.2 U{I} := {parsePrint(u)}; ", sep="", end="\n")
    #print(u, "\n")

    #calculam s prim

    for i in s:
        i.sort()

    for i in tNegat:
        i.sort()

    for i in tSimplu:
        i.sort()


    for i in tNegat:
        if i in s:
            s.remove(i)

    for i in tSimplu:
        if i in s:
            s.remove(i)

    #note vlod: posibil să fie duplicate
    s.extend(u)
    #print(s, "\n")

    #s2` eliminam clauzele triviale din s`

    toRemove = []
    for i in s:
        if clauzaTriviala(i):
            toRemove.append(i)
    
    for i in toRemove:
        s.remove(i)
        #chck patratel
        if clauzaPurTriviala(i):
            s.append([])


    print(f"P{I}.3 S{I} := {parsePrint(s)}; ", sep="", end="\n")
    #print(s, "\n")

    print(f"P{I}.4 ", sep="", end="")

    if s == []:
        print("S este satisfiabilă")
        break
    elif [] in s:
        print("S nu e satisfiabilă")
        break
    else:
        I += 1
        print(f"i := {I} and go to P{I}.1.")
        
