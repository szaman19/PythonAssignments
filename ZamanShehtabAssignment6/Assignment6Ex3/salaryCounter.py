#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 6: Problem 3

'''
Analysis

The purpose of this program is to calculate how a single penny grows over 
a given number of days, if it is doubled every day. 

Output to monitor:
  table of day and the current salary corresponding to that day.
  horizontalPrintLine() prints a horizontal line equal to the screen length  
  finalAmount (float) - The total salary after the given number of days.


Input from keyboard:
  numOfDaysInt (int) - The number of days to calculate the salary for. 

Tasks allocated to Functions: 
  errorCheck(string) - returns a string if invalid input or empty string and
                       the int value of the input if valid input 
  pennyCalculator(int, int) - returns a list containing the current day and
                              its corresponding salary value. 
  horizontalPrintLine() - returns a string that creates a dashed line on 
                          the monitor

'''

DOLLAR_CONVERTER = 100
LINE_LENGTH = 105
DOUBLE = 2
INITIAL_STAGE_ONE = 1
INCREMENT = 1
INDEX_OF_DAY = 0
INDEX_OF_PAY = 1

def errorCheck(stringInput):
  errorMessage=""
  try:
    intResult = int(stringInput)
    if intResult <=0:
      #print("This program only takes in natural number values.\
      # Please try again")
      errorMessage = "Invalid"
  except ValueError:
    if stringInput =='':
      errorMessage = "Close"
    else:
      #print("This program only takes in natural number values.\
      # Please try again")
      errorMessage = "Invalid"
  #print (errorMessage)
  return (errorMessage or intResult)

def pennyCalculator(numDay, currentPennyVal):
  day = numDay + INCREMENT
  pennyVal = currentPennyVal * DOUBLE
  return [day,pennyVal]

def horizontalPrintLine():
  line = ""
  for dash in range(0,LINE_LENGTH):
    line +="-"
  return line

def main():
  inputMessage = "Enter the number of days for which salary is to be \
    computed(or press <Enter> to quit): "
  invalidInputMessage = "This program only takes in natural number \
    values. Please try again"

  numOfDaysStr = input(inputMessage)

  numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr)
  
  while numOfDaysErrorCheckedInt == "Invalid":
    print(invalidInputMessage)
    numOfDaysStr = input(inputMessage)
    numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr)

  if numOfDaysErrorCheckedInt == "Close":
    numOfDaysErrorCheckedInt = False
    
  
  while numOfDaysErrorCheckedInt:
    day = INITIAL_STAGE_ONE
    pay = INITIAL_STAGE_ONE
    totalPay = INITIAL_STAGE_ONE
    
    print("{0:4} {1:96} {2:4}".format("Day"," ","Pay"))
    print(horizontalPrintLine())
    print("{0:4} {1:100}".format(day,pay))
    
    while day < numOfDaysErrorCheckedInt:
      resultList = pennyCalculator(day,pay)
      day = resultList[INDEX_OF_DAY]
      pay = resultList[INDEX_OF_PAY]
      totalPay += pay
      print("{0:4} {1:100}".format(day,pay))

    finalAmount = totalPay / DOLLAR_CONVERTER
    print(horizontalPrintLine())
    print("In ",numOfDaysErrorCheckedInt,"days a penny grows to $",\
      "{:.2f}".format(finalAmount))
    print(horizontalPrintLine())
    numOfDaysStr = input(inputMessage)

    numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr)
    
    while numOfDaysErrorCheckedInt == "Invalid":
      print(invalidInputMessage)
      numOfDaysStr = input(inputMessage)
      numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr)
   
    if numOfDaysErrorCheckedInt == "Close":
      numOfDaysErrorCheckedInt = False

  # tester1 = [4,14,30,365]
  # tester2 = [0.15,163.83,10737418.23,751533626487626648569070089221\
  #   4409913018813026346866355016103742446972929222333529500320616655\
  #    51888458711040.00]
  # for testNum in range(len(tester1)):
  #   if pennyCalculator(tester1[testNum]) == tester2[testNum]:
  # 	  print("The program passed the test for the value ",tester1[testNum])
  #   else:
  #     print("The program did not pass the test")
    	

main()