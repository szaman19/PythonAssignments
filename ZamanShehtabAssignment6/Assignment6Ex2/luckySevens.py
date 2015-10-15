#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 6: Problem 2
'''

Restate the problem

(Note:  only list categories that apply)

Output to monitor:
  variableName1 (variableType) - description
  variableName2 (variableType) - description
  etc.
  (if no variable name, just describe what is output along with its type)
Output to window: 
  describe what is drawn, etc.
Output to file:
  describe what is written to file
  
Input from keyboard:
  (Note:  you can list converted variables here,
          rather than clutter the section with
          string versions that must be converted)
  variableName1 (variableType) - description
  etc.
Tasks allocated to Functions:
  name and description of functions that YOU write
'''

import random

LINE_LENGTH = 19
DICE_MIN = 1
DICE_MAX = 7
LUCKY_SEVEN = 7
LUCKY_SEVEN_PRIZE = 4
INCREMENT = 1

INDEX_OF_TURN = 0
INDEX_OF_DIE_VALUE = 1
INDEX_OF_MONEY_LEFT=2
INDEX_OF_MAX_TURN = 3
INDEX_OF_MAXIMUM = 4
def throwDie():
  dice1 = random.randrange(DICE_MIN,DICE_MAX)
  dice2 = random.randrange(DICE_MIN,DICE_MAX)
  return dice1 + dice2

def isMax(currentMax,newVal):
  return newVal > currentMax

def runGame(startingMoney, turnNum,currentMax,currentMaxTurn):
  moneyLeft = startingMoney
  turn = turnNum
  maximum = currentMax
  maxTurn = currentMaxTurn
  dieValue = throwDie()
  if(dieValue == LUCKY_SEVEN):
    moneyLeft += LUCKY_SEVEN_PRIZE
    turn += INCREMENT
    if isMax(maximum,moneyLeft):
      maximum = moneyLeft
      maxTurn = turn    
    #print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
  else:
    moneyLeft -= INCREMENT
    turn +=INCREMENT
    #print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
  return [turn,dieValue,moneyLeft,maxTurn,maximum]

def errorCheck(stringInput):
  #errorMessage = ""
  try:
    intResult = int(stringInput)
  except ValueError:
    # if stringInput =='':
    #   intResult = "Close"
    # else:
    #   #print("This program only takes in whole number values. Please try again")
      intResult = False
  return intResult

def horizontalPrintLine():
  line = ""
  for dash in range(0,LINE_LENGTH):
    line +="-"
  return line

def main():
  inputMessage = "Please place your bet in whole dollars: OR press <Enter> to quit:  "
  errorMessage = "This program only takes in whole number values. Please try again"
  
  potSizeStr = input(inputMessage)
  
  


  while(potSizeStr):

    potSizeIntErrorChecked = errorCheck(potSizeStr)
    while not potSizeIntErrorChecked:
      print(errorMessage)
      potSizeStr = input(inputMessage)
      potSizeIntErrorChecked = errorCheck(potSizeStr)
    
    print('{0:5} {1:5} {2:8}'.format("Roll","Value","Dollars"))
    print(horizontalPrintLine())

    maximum = potSizeIntErrorChecked
    maxTurn = 0
    turn = 0
    moneyLeft = potSizeIntErrorChecked

    while moneyLeft > 0:
      resultList = runGame(moneyLeft,turn,maximum,maxTurn)
      turn = resultList[INDEX_OF_TURN]
      dieValue = resultList[INDEX_OF_DIE_VALUE]
      moneyLeft =resultList[INDEX_OF_MONEY_LEFT]
      maxTurn = resultList[INDEX_OF_MAX_TURN]
      maximum = resultList[INDEX_OF_MAXIMUM]
      
      print('{0:5d} {1:4d} {2:7d}'.format(turn,dieValue,moneyLeft))
    maxOutput = '$'+str(maximum)
    
    print("You became broke after ",turn," rolls")
    print("You should have quit after",maxTurn," rolls when you had",maxOutput,"\n")				
    
    potSizeStr = input(inputMessage)

main()
