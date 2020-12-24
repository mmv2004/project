"""
######################################################################
  Программа для ГЕНЕРАЦИИ задач типа 26(С3), аналогичных демо-варианту
  ЕГЭ по информатике 2016 года
  (C) К.Ю. Поляков, 2015
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Демо-вариант 2016 года (ФИПИ)
# http://fipi.ru/sites/default/files/document/1440408722/inf-11_2016.zip
# Вариант с двумя возможными ходами
#-----------------------------------------------------------------
# GAME OVER - условие окончания игры
#-------------------------------------------------------
def GameOver(n1, n2):
    global TARGET
    return n1+n2 >= TARGET

#-------------------------------------------------------
# Демо-вариант ЕГЭ-2016
#-------------------------------------------------------
TARGET = 38
N1 = 5 
def Oper1(n1, n2): return (n1+1, n2)
def Oper2(n1, n2): return (n1*2, n2)
operations = [Oper1, Oper2]

#-------------------------------------------------------
# Новый вариант 
#-------------------------------------------------------
TARGET = 38
N1 = 4 
def Oper1(n1, n2): return (n1+2, n2)
def Oper2(n1, n2): return (n1*2, n2)
operations = [Oper1, Oper2]

#-------------------------------------------------------
# Определяем минимальное количество камней во второй куче
# для выигрыша первым ходом
#-------------------------------------------------------
n2min = TARGET
for op in operations:
  n2 = 1
  while True:
    if GameOver(*op(N1,n2)) or \
      GameOver(*op(n2,N1)): break; 
    n2 += 1
  if n2 < n2min: 
    n2min = n2  
print ( n2min )

print("-------------------------------------------------------")
print("Задача 26(С3) по образцу демо-варианата ЕГЭ-2016  ")
print("-------------------------------------------------------")
print('Число камней для окончания игры:', TARGET)

#-------------------------------------------------------
# EVALUATE POSITION - определение типа позиции
#   (выигрышная или проигрышная) и числа ходов до
#   окончания игры
#-------------------------------------------------------
def EvaluatePosition(pos, operations):
    global nest
    if pos in positionTable:
        return positionTable[pos]
    winSteps = -1
    lossSteps = -1
    n1, n2 = pos
    #----------------------------------------------
    def handle(result, steps):
        nonlocal lossSteps, winSteps
        if result == "W":
            if steps > lossSteps: lossSteps = steps
        else:
            steps += 1
            if winSteps < 0  or steps < winSteps:
                winSteps = steps                    
    #----------------------------------------------
    for op in operations:
        if GameOver(*op(n1,n2)) or \
           GameOver(*op(n2,n1)): 
            res = ("W", 1)    
            positionTable[pos] = res
            return res       
    for op in operations:
        nextPos = op(n1, n2)        
        (result, steps) = EvaluatePosition(nextPos, operations)
        handle(result, steps)
        nextPos = op(n2, n1)[::-1]        
        (result, steps) = EvaluatePosition(nextPos, operations)
        handle(result, steps)
    if winSteps >= 0:
          res = ("W", winSteps)
    else: res = ("x", lossSteps)
    positionTable[pos] = res
    return res

#-------------------------------------------------------
# Заполнение таблицы, указывающей выигрышные и
# проигрышные позиции
#-------------------------------------------------------
pos1 = []
pos2 = []
pos3 = []
pos4 = []

outStr = 10*[""]
for i in range(n2min,n2min-10,-1):
    outStr[n2min-i] = "%2d: " % i
header = "   "

ans1a = []
ans1b = []
ans2 = []
ans3 = []

for N1x in range(N1,N1+7):
  header = header + (" %2d " % N1x)  
  positionTable = {}
  for i in range(TARGET-N1x-1,0,-1):
      r, steps = EvaluatePosition((N1x,i), operations)
      if r == "W":
          if n2min-9 <= i <= n2min: 
              # print("%2d: +%d " % (i, steps))
              outStr[n2min-i] = outStr[n2min-i] + (" %d  " % steps)
              if steps == 2:
                pos2.append( (N1x,i) )
              if steps == 3:
                pos4.append( (N1x,i) )
          if steps == 1: ans1a.insert(0,i)
          if steps == 2: ans2.insert(0,i)
      else:
          if i >= n2min-9: 
              #print("%2d:  %d" % (i, steps))
              outStr[n2min-i] = outStr[n2min-i] + ("-%d  " % steps)
              if steps == 1:
                pos1.append( (N1x,i) )
              if steps == 2:
                pos3.append( (N1x,i) )
          if steps == 1: ans1b.insert(0,i)
          if steps == 2: 
              for op in operations:
                  nextPos = op(N1x, i)
                  (result,steps) = EvaluatePosition(nextPos, operations)
                  if steps == 1:
                      if not i in ans3:
                          ans3.insert(0,i)
                          break
                  nextPos = op(i, N1x)[::-1]
                  (result,steps) = EvaluatePosition(nextPos, operations)
                  if steps == 1:
                      if not i in ans3:
                          ans3.insert(0,i)
                          break

print ( header )
for s in outStr:
  print ( s )
#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Позиции по заданиям ---")
print(" Задание 1: " + str(pos1))
print(" Задание 2: " + str(pos2))
print(" Задание 3: " + str(pos3))
print(" Задание 4: " + str(pos4))

