import random

def throwDie():
  dice1 = random.randrange(1,7)
  dice2 = random.randrange(1,7)
  return dice1 + dice2

def runGame(startingMoney):
  maximum = startingMoney
  maxTurn = 0
  turn = 0
  moneyLeft = startingMoney
  print('{0:5} {1:5} {2:8}'.format("Roll","Value","Dollars"))
  while(moneyLeft > 0):
    dieValue = throwDie()
    if(dieValue == 7):
      moneyLeft += 4
      turn += 1
      if(moneyLeft > maximum):
        maximum = moneyLeft
        maxTurn = turn
      
      print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
    else:
      moneyLeft -= 1
      turn +=1
      print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
  maxOutput ="$"+str(maximum)
  print("You became broke after ",turn," rolls")
  print("You should have quit after",maxTurn," rolls when you had",maxOutput)

def errorCheck(stringInput):
  try:
    intResult = int(stringInput)
  except ValueError:
    if stringInput =='':
      intResult = False
    else:
      print("This program only takes in whole number values. Please try again")
      retry = input("Please place your bet in whole dollars: OR press <Enter> to quit:  ")
      intResult = errorCheck(retry)
  return intResult

def main():
  potSizeStr = input("Please place your bet in whole dollars: OR press <Enter> to quit:  ")
  potSizeIntErrorChecked = errorCheck(potSizeStr)
  while(potSizeIntErrorChecked):
    runGame(potSizeIntErrorChecked)				
    potSizeStr = input("Please place your bet in whole dollars: OR press <Enter> to quit:  ")
    potSizeIntErrorChecked = errorCheck(potSizeStr)

main()
