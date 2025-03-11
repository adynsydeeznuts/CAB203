def Q1A(n):
    if n == 0: return 0
    else: return 2 - Q1A(n-1)


def Q1B(n):
    if n == 0 or n == 1: return 1
    else: return Q1B(n-1) - Q1B(n-2)

def Q1C(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1
    else: return Q1C(n-1) - Q1C(n-2) + 2*Q1C(n-3)

def Q2A(x, y, z):
    return (not x or y) and z

def AndFormula(x, y):
    return x and y

def NANDFormula(x, y):
    return not(x and y)

def NORFormula(x, y):
    return not x or not y

def Q2B(f):
    trueCount = 0
    falseCount = 0

    tautology = False
    contradiction = False
    satisfiable = False
    contingent = False

    for i in range(0,2):
        for j in range(0,2):
            if f(i, j) == 0: falseCount += 1
            else: trueCount += 1

    if(falseCount == 4): contradiction = True
    if(trueCount == 4): tautology = True
    if(trueCount > 0): satisfiable = True
    if(trueCount > 0 and falseCount > 0): contingent = True

    return f'Contradiction: {contradiction} \n Tautology: {tautology} \n Satisfiable: {satisfiable} \n Contingent: {contingent}'


def Q2C(f1, f2):
    truthTableCol1 = []
    truthTableCol2 = []

    for i in range(0,2):
        for j in range(0,2):
            truthTableCol1.append(f1(i,j))
            truthTableCol2.append(f2(i,j))
    
    if(truthTableCol1 == truthTableCol2): return "equivalent"
    else: return "not equivalent"
            


print(Q2C(NANDFormula, AndFormula))
