#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 6: Problem 2
'''

Analysis

This program simulates a lucky sevens game where it asks for the starting bet
and then simulates throwing dice and calculates when the pot reaches the
highest amount. 

Output to monitor:
  turn(int) 
  diceValue(int)
  moneyLeft(int)
  maxTurn(int) - The turn in which player had the most money
  maxOutput(int) - The most money the player had during the game
  
Input from keyboard:
  potSizeIntErrorChecked - The starting bet 

Tasks allocated to Functions:
  throwDice() - Simulates throwing two dice and returns their sum 
  isMax(currentMax,newVal) - Checks if newVal is greater than currentMax
  runGame(startingMoney,turnNum,currentMax,currentMaxTurn) - 
     given startingMoney, turnNum, currentMax, currentMaxTurn, calls
     throwDice() and changes startingMoney, turnNum, currentMax, 
     currentMaxTurn accordingly.  
  errorCheck(stringInput) - given stringInput, checks if it is an int >0
  horizontalPrintLine() - Creates a horizontal line on output 

'''
#Imports 
import random

#Global Constants 
LINE_LENGTH = 19
DICE_MIN = 1
DICE_MAX = 7
LUCKY_SEVEN = 7
LUCKY_SEVEN_PRIZE = 4
INCREMENT = 1

INDEX_OF_TURN = 0
INDEX_OF_DICE_VALUE = 1
INDEX_OF_MONEY_LEFT=2
INDEX_OF_MAX_TURN = 3
INDEX_OF_MAXIMUM = 4

#No params
#Simulates throwing two dice and returns their sum
#Returns int 
def throwDice():
  dice1 = random.randrange(DICE_MIN,DICE_MAX)
  dice2 = random.randrange(DICE_MIN,DICE_MAX)
  return dice1 + dice2

#Two Params, (int,int)
#Checks if newVal > currentMax
#Returns bool
def isMax(currentMax,newVal):
  return newVal > currentMax

#Four Params (int,int,int,int)
#given the inputs, simulates on turn of lucky sevens. Calls throwdice() and 
#if the value is 7, increases moneyLeft and checks isMax(), otherwise
#decreases moneyLeft and increments turns
#Returns a list of ints 
def runGame(startingMoney, turnNum,currentMax,currentMaxTurn):
  moneyLeft = startingMoney
  turn = turnNum
  maximum = currentMax
  maxTurn = currentMaxTurn

  #Simulates throwing two dice
  diceValue = throwDice()
  if(diceValue == LUCKY_SEVEN):
    moneyLeft += LUCKY_SEVEN_PRIZE
    turn += INCREMENT
    if isMax(maximum,moneyLeft):
      maximum = moneyLeft
      maxTurn = turn    
    #print('{0:5d} {1:4d} {2:7d}'.format(turn,diceValue,moneyLeft))
  else:
    moneyLeft -= INCREMENT
    turn +=INCREMENT
    #print('{0:5d} {1:4d} {2:7d}'.format(turn,diceValue,moneyLeft))
  return [turn,diceValue,moneyLeft,maxTurn,maximum]

#One Param (string)
#Checks if string can be  converted to int 
#Returns int or False 
def errorCheck(stringInput):
  #errorMessage = ""
  try:
    intResult = int(stringInput)
  except ValueError:
      intResult = False
  return intResult
#No Params
#Creates a string with give LINE_LENGTH
#Returns string
def horizontalPrintLine():
  line = ""
  for dash in range(0,LINE_LENGTH):
    line +="-"
  return line

#Asks user for number of days to calculate salary for and prints out table
def main():
  inputMessage = "Please place your bet in whole dollars: OR press <Enter> to quit:  "
  errorMessage = "This program only takes in whole number values. Please try again"
  
  #Priming read 
  potSizeStr = input(inputMessage)
  
  #Continuation Loop
  while(potSizeStr):
    
    #Validation Loop 
    potSizeIntErrorChecked = errorCheck(potSizeStr)
    while not potSizeIntErrorChecked:
      print(errorMessage)
      potSizeStr = input(inputMessage)
      potSizeIntErrorChecked = errorCheck(potSizeStr)
    
    #Header print 
    print('{0:5} {1:5} {2:8}'.format("Roll","Value","Dollars"))
    print(horizontalPrintLine())
    
    #Initial Stage 
    maximum = potSizeIntErrorChecked
    maxTurn = 0
    turn = 0
    moneyLeft = potSizeIntErrorChecked
    
    #Simulation 
    while moneyLeft > 0:
      resultList = runGame(moneyLeft,turn,maximum,maxTurn)
      turn = resultList[INDEX_OF_TURN]
      diceValue = resultList[INDEX_OF_DICE_VALUE]
      moneyLeft =resultList[INDEX_OF_MONEY_LEFT]
      maxTurn = resultList[INDEX_OF_MAX_TURN]
      maximum = resultList[INDEX_OF_MAXIMUM]
      
      print('{0:5d} {1:4d} {2:7d}'.format(turn,diceValue,moneyLeft))
    maxOutput = '$'+str(maximum)
    
    #Final Output
    print("You became broke after ",turn," rolls")
    print("You should have quit after",maxTurn," rolls when you had",maxOutput,"\n")				
    #<--End of simulation

    #Continuation read 
    potSizeStr = input(inputMessage)

main()
