
def parseString(s):
    s = str(s)
    s = s.replace(" ", "")
    s = s.replace("->", ">")
    
    for i in s:
        if i not in ">01&|()" and not i.isalpha():
            raise Exception("sintax error")
    
            
    return s

def parseConstantsOneExpression(s):
    
    state = "var1"
    var1 = " "
    var2 = " "
    operand = " "

    for i in s:
        if state == "var1":
            var1 = i

        elif state == "var2":
            var2 = i

        elif state == "op":
            operand = i

        else:  
           raise Exception("")  


    return 0




print(parseString("a -> b & b -> a "))