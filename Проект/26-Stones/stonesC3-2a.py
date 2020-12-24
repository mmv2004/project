"""
######################################################################
  Программа для решения задач типа С3, аналогичных досрочному варианту
  ЕГЭ по информатике 2015 года
  (C) К.Ю. Поляков, 2015
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Досрочный вариант 2015 года (ФИПИ)
# http://www.fipi.ru/sites/default/files/document/2015/05.pdf
# Вариант с двумя возможными ходами
#-----------------------------------------------------------------
TARGET = 55
N1 = 5 
def Oper1(n1, n2): return (n1+1, n2)
def Oper2(n1, n2): return (n1*2, n2)
operations = [Oper1, Oper2]

#-----------------------------------------------------------------
TARGET = 80
N1 = 7 
def Oper1(n1, n2): return (n1+2, n2)
def Oper2(n1, n2): return (n1*2, n2)
operations = [Oper1, Oper2]

print("-------------------------------------------------------")
print("    Решение задачи C26 из досрочного варианта ЕГЭ-2015  ")
print("-------------------------------------------------------")
print('Число камней для окончания игры:', TARGET)

#-------------------------------------------------------
# GAME OVER - условие окончания игры
#-------------------------------------------------------
def GameOver(n1, n2):
    global TARGET
    return n1+n2 >= TARGET

#-------------------------------------------------------
# EVALUATE POSITION - определение типа позиции
#   (выигрышная или проигрышная) и числа ходов до
#   окончания игры
#-------------------------------------------------------
nest = 0
def margin(n):
    for i in range(n):
        print("  ", end="", sep="")
def show(pos, add = ""):
    if 0:
      margin(nest)
      print(pos, add)
    
def EvaluatePosition(pos, operations):
    global nest
    if pos in positionTable:
        return positionTable[pos]
    winSteps = -1
    lossSteps = -1
    n1 = pos[0]; n2 = pos[1]
    show(pos)
    def handle(result, steps):
        nonlocal lossSteps, winSteps
        if result == "W":
            if steps > lossSteps: lossSteps = steps
        else:
            steps += 1
            if winSteps < 0  or steps < winSteps:
                winSteps = steps                
    
    for op in operations:
        if GameOver(*op(n1,n2)) or \
           GameOver(*op(n2,n1)): 
            res = ("W", 1)    
            show(pos, res)
            positionTable[pos] = res
            return res
        
    for op in operations:
        nextPos = op(n1, n2)        
        nest += 1
        (result, steps) = EvaluatePosition(nextPos, operations)
        nest -= 1    
        handle(result, steps)
        p = op(n2, n1)        
        nextPos = (p[1], p[0])
        nest += 1
        (result, steps) = EvaluatePosition(nextPos, operations)
        nest -= 1    
        handle(result, steps)
    if winSteps >= 0:
          res = ("W", winSteps)
    else: res = ("x", lossSteps)
    show(pos, res)
    positionTable[pos] = res
    return res

#-------------------------------------------------------
# Заполнение таблицы, указывающей выигрышные и
# проигрышные позиции
#-------------------------------------------------------
ans1a = []
ans1b = []
ans2 = []
ans3 = []
positionTable = {}

for i in range(TARGET-N1-1,0,-1):
    r, steps = EvaluatePosition((N1,i), operations)
    if r == "W":
        print("%2d: выигрыш (%d) " % (i, steps))
        if steps == 1: ans1a.insert(0,i)
        if steps == 2: ans2.insert(0,i)
    else:
        print("%2d: :-( (%d)" % (i, steps))
        if steps == 1: ans1b.insert(0,i)
        if steps == 2: 
            for op in operations:
                nextPos = op(N1, i)
                (result,steps) = EvaluatePosition(nextPos, operations)
                if steps == 1:
                    if not i in ans3:
                        ans3.insert(0,i)
                        break
                nextPos = op(i, N1)
                nextPos = (nextPos[1],nextPos[0])
                (result,steps) = EvaluatePosition(nextPos, operations)
                if steps == 1:
                    if not i in ans3:
                        ans3.insert(0,i)
                        break

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print(" Вопрос 1а: " + str(ans1a))
print(" Вопрос 1б: " + str(ans1b))
print(" Вопрос 2:  " + str(ans2))
print(" Вопрос 3:  " + str(ans3))

