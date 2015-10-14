DOLLAR_CONVERTER = 100
def errorCheck(stringInput):
  errorMessage=""
  try:
    intResult = int(stringInput)
    if intResult <=0:
      #print("This program only takes in natural number values. Please try again")
      errorMessage = "Invalid"
  except ValueError:
    if stringInput =='':
      errorMessage = "Close"
    else:
      #print("This program only takes in natural number values. Please try again")
      errorMessage = "Invalid"
  #print (errorMessage)
  return (errorMessage or intResult)
def pennyCalculator(numDay, currentPennyVal):
  day = numDay + 1
  pennyVal = currentPennyVal * 2
  return [day,pennyVal]
def horizontalPrintLine():
  line = ""
  for dash in range(0,105):
    line +="-"
  return line

def main():
  inputMessage = "Enter the number of days for which salary is to be computed(or press <Enter> to quit): "
  invalidInputMessage = "This program only takes in natural number values. Please try again"

  numOfDaysStr = input(inputMessage)

  numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr)
  while numOfDaysErrorCheckedInt == "Invalid":
    print(invalidInputMessage)
    numOfDaysStr = input(inputMessage)
    numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr)

  if numOfDaysErrorCheckedInt == "Close":
    numOfDaysErrorCheckedInt = False
    
  
  while numOfDaysErrorCheckedInt:
    day = 1
    pay = 1
    totalPay = 1
    print("{0:4} {1:96} {2:4}".format("Day"," ","Pay"))
    print(horizontalPrintLine())
    print("{0:4} {1:100}".format(day,pay))
    while day < numOfDaysErrorCheckedInt:
      resultList = pennyCalculator(day,pay)
      day = resultList[0]
      pay = resultList[1]
      totalPay += pay
      print("{0:4} {1:100}".format(day,pay))

    finalAmount = totalPay / DOLLAR_CONVERTER
    print(horizontalPrintLine())
    print("In ",numOfDaysErrorCheckedInt,"days a penny grows to $","{:.2f}".format(finalAmount))
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
  # tester2 = [0.15,163.83,10737418.23,751533626487626648569070089221440991301881302634686635501610374244697292922233352950032061665551888458711040.00]
  # for testNum in range(len(tester1)):
  #   if pennyCalculator(tester1[testNum]) == tester2[testNum]:
  # 	  print("The program passed the test for the value ",tester1[testNum])
  #   else:
  #     print("The program did not pass the test")
    	

main()