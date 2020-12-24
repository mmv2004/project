"""
######################################################################
  Программа для решения задач типа С3, аналогичных боевым вариантам
  ЕГЭ по информатике 2016 года
  (C) К.Ю. Поляков, 2016
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Вариант с двумя возможными ходами
#-----------------------------------------------------------------
MAX_STONES = 24
OVER_STONES = 38
def Oper1(n): return n+1
def Oper2(n): return n*2
operations = [Oper1, Oper2]

MAX_STONES = 35
OVER_STONES = 58
def Oper1(n): return n+1
def Oper2(n): return n*2
operations = [Oper1, Oper2]

print("-------------------------------------------------------")
print("    Решение задачи 26 (C3) из вариантов ЕГЭ-2016       ")
print("-------------------------------------------------------")
print('Число камней для окончания игры:', MAX_STONES)
print('Перебор для количества камней более:', OVER_STONES)

#-------------------------------------------------------
# GAME OVER - условие окончания игры
#-------------------------------------------------------
def GameOver(n):
    global MAX_STONES, OVER_STONES    
    if n >= MAX_STONES:
      if n <= OVER_STONES:
          return 1
      else: 
          return -1
    return 0
#-------------------------------------------------------
# EVALUATE POSITION - определение типа позиции
#   (выигрышная или проигрышная) и числа ходов до
#   окончания игры
#-------------------------------------------------------
def EvaluatePosition(n, operations):
    winSteps = -1
    lossSteps = -1
    for op in operations:
        res = GameOver(op(n))
        if res == 1: return ("W", 1)    
    for op in operations:
        nextVal = op(n)
        try:
          (result,steps) = positionTable[nextVal]
        except:
          continue;        
        if result == "W":
            if steps > lossSteps: lossSteps = steps
        else:
            steps += 1
            if winSteps < 0  or steps < winSteps:
                winSteps = steps                
    if winSteps >= 0:
          return ("W", winSteps)
    else: return ("x", lossSteps)

#-------------------------------------------------------
# Заполнение таблицы, указывающей выигрышные и
# проигрышные позиции
#-------------------------------------------------------
ans1a = []
positionTable = {}
for i in range(MAX_STONES-1,0,-1):
    positionTable[i] = EvaluatePosition(i, operations)
    r, steps = positionTable[i]
    if r == "W":
        print("%2d: выигрыш (%d) " % (i, steps))
        if steps == 1: ans1a.insert(0,i)
    else:
        print("%2d: :-( (%d)" % (i, steps))
#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print(" Вопрос 1а: " + str(ans1a))

