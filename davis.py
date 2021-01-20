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
    


#s = [ ["1", "!3"], ["2", "1"], ["2", "!1", "3"]]
s = [ ["!1", "2", "!4"], ["!3", "!2"], ["1", "3"], ["1"], ["3"], ["4"]]

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

    print(tSimplu)
    print(tNegat, '\n')

    tSimpluEliminat = deepcopy(tSimplu)    
    tNegatEliminat = deepcopy(tNegat)

    for i in tSimpluEliminat:
        if x in i:
            i.remove(x)

    for i in tNegatEliminat:
        if "!" + x in i:
            i.remove("!" + x)

    print(tSimpluEliminat)
    print(tNegatEliminat, "\n")

    u = []

    if tSimplu != [] and tNegat != []:
        for i in tSimpluEliminat:
            cur = i
            for j in tNegatEliminat:
                cur += j

            u+=[cur]

    print(u, "\n")

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
    print(s, "\n")

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


    print(s, "\n")

    if s == []:
        print("S este satisfiabilă")
        break
    elif [] in s:
        print("S e nesatisfiabilă")
        break
    else:
        pass
        #i++
