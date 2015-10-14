import random

def throwDie():
  dice1 = random.randrange(1,7)
  dice2 = random.randrange(1,7)
  return dice1 + dice2

def isMax(currentMax,newVal):
  return newVal > currentMax

def runGame(startingMoney, turnNum,currentMax,currentMaxTurn):
  moneyLeft = startingMoney
  turn = turnNum
  maximum = currentMax
  maxTurn = currentMaxTurn
  dieValue = throwDie()
  if(dieValue == 7):
    moneyLeft += 4
    turn += 1
    if isMax(maximum,moneyLeft):
      maximum = moneyLeft
      maxTurn = turn    
    #print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
  else:
    moneyLeft -= 1
    turn +=1
    #print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
  return [turn,dieValue,moneyLeft,maxTurn,maximum]
def isBool(unknownInput):
  return type(unknownInput) == bool

def errorCheck(stringInput):
  try:
    intResult = int(stringInput)
  except ValueError:
    if stringInput =='':
      intResult = True
    else:
      #print("This program only takes in whole number values. Please try again")
      intResult = False
  return intResult

def main():
  inputMessage = "Please place your bet in whole dollars: OR press <Enter> to quit:  "
  errorMessage = "This program only takes in whole number values. Please try again"
  potSizeStr = input(inputMessage)
  potSizeIntErrorChecked = errorCheck(potSizeStr)
  
  while not potSizeIntErrorChecked:
    print(errorMessage)
    potSizeStr = input(inputMessage)
    potSizeIntErrorChecked = errorCheck(potSizeStr)

  if isBool(potSizeIntErrorChecked):
    potSizeIntErrorChecked = False

  while(potSizeIntErrorChecked):
    
    print('{0:5} {1:5} {2:8}'.format("Roll","Value","Dollars"))
    
    maximum = potSizeIntErrorChecked
    maxTurn = 0
    turn = 0
    moneyLeft = potSizeIntErrorChecked

    while moneyLeft > 0:
      resultList = runGame(moneyLeft,turn,maximum,maxTurn)
      turn = resultList[0]
      dieValue = resultList[1]
      moneyLeft =resultList[2]
      maxTurn = resultList[3]
      maximum = resultList[4]
      print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
    maxOutput = '$'+str(maximum)
    
    print("You became broke after ",turn," rolls")
    print("You should have quit after",maxTurn," rolls when you had",maxOutput)				
    
    potSizeStr = input(inputMessage)
    potSizeIntErrorChecked = errorCheck(potSizeStr)

    while not potSizeIntErrorChecked:
      print(errorMessage)
      potSizeStr = input(inputMessage)
      potSizeIntErrorChecked = errorCheck(potSizeStr)

    if isBool(potSizeIntErrorChecked):
      potSizeIntErrorChecked = False

main()
