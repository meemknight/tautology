import itertools
import sys

class LogicalSintaxError(Exception):
    pass


operands = "!>&|="

def parseString(s):
    s = str(s)
    s = s.replace(" ", "")
    s = s.replace("\n", "")
    s = s.replace("<->", "=")
    s = s.replace("->", ">")
    s = s.replace("V", "|")
    s = s.replace("^", "&")
    
    for i in s:
        if i not in operands + "()" + "01" and not i.isalpha():
            raise LogicalSintaxError()
    
            
    return s

def implication(a, b):
    if(a == True and b == False):
        return False
    return True

def negation(a):
    return not a

def parseOneExpression(v1, op, v2):
    
    v1 = True if v1 == '1' else False
    v2 = True if v2 == '1' else False

    returnVal = ""

    if op == ">":
        returnVal = implication(v1, v2)
    elif op == "&":
        returnVal = v1 and v2
    elif op == "|":
        returnVal = v1 or v2
    elif op == "=":
        returnVal = (v1 == v2)
    else:
        raise LogicalSintaxError()
    
    return "1" if returnVal else "0"

def parseConstantsLinearExpression(s):
    
#handle negations
    while True:
        if "!0" in s or "!1" in s:
            s = s.replace("!1", "0")
            s = s.replace("!0", "1")
        elif "!" in s:
            raise LogicalSintaxError()
        else:
            break

    state = "var1"
    var1 = "0"
    var2 = " "
    operand = " "

    for i in s:
        if state == "var1":
            var1 = i
            if var1 != '0' and var1 !='1':
                raise LogicalSintaxError()
            state = "op"


        elif state == "var2":
            var2 = i
            if var2 != '0' and var2 !='1':
                raise LogicalSintaxError()
            state = "op"
            var1 = parseOneExpression(var1, operand, var2)


        elif state == "op":
            operand = i
            if operand not in operands:
                raise LogicalSintaxError()
            state = "var2"


        else:  
           raise Exception("")  


    return var1

def parseConstantsMoreExpressions(s):

    while "(" in s or ")" in s:
        pos = 0
        lastOpen = -1

        for i in s:
            if i == "(":
                lastOpen = pos
            elif i == ")":
                if lastOpen == -1:
                    raise LogicalSintaxError()
                else:
                    s = s[:lastOpen] + parseConstantsLinearExpression(s[lastOpen+1:pos]) + s[pos+1:]
                    lastOpen = -1
                    break
            pos += 1

        if lastOpen != -1:
            raise LogicalSintaxError()

    return parseConstantsLinearExpression(s)

def parseComplexExpression(s):
    print(s)
    print("")
    s = parseString(s)

    letters = []

    for i in s:
        if i.isalpha() and i not in letters:
            letters.append(i)

    letters.sort()

    it = itertools.product ([0,1],  repeat= len(letters) )

    for letter in letters:
        print(letter + " ", end = "")
    print("")

    for i in it:
        temp = s

        count = 0
        for letter in letters:
            temp = temp.replace(letter, str(i[count]))
            print(str(i[count]) + " ", end = "")
            count += 1

        print (parseConstantsMoreExpressions(temp))



try:

    #s  = sys.argv[1]
    
    #parseComplexExpression('((a->b) & (b->a)) -> (!(a&!(b)))')
    parseComplexExpression('a ^ b')
except LogicalSintaxError:
    print("Sintax error")


#todo rename main
#todo fnd fnc
#todo davis putman 135
