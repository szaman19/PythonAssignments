DOLLAR_CONVERTER = 100
def errorCheck(stringInput, inputMessage):

  try:
    intResult = int(stringInput)
    if intResult <=0:
      print("This program only takes in natural number values. Please try again")
      retry = input(inputMessage)
      intResult = errorCheck(retry, inputMessage)
  except ValueError:
    if stringInput =='':
      intResult = False
    else:
      print("This program only takes in natural number values. Please try again")
      retry = input(inputMessage)
      intResult = errorCheck(retry, inputMessage)
  
  return intResult  

def salaryCalculator(numDays):
  day = 1
  pay = 1
  totalPay = 1
  print("{0:4}{1:100}{2:4}".format("Day"," ","Pay"))
  print("{0:4} {1:100}".format(day,pay))
  while day < numDays:
    day += 1
    pay = pay * 2
    totalPay += pay
    print("{0:4} {1:100}".format(day,pay))
  
  return totalPay / DOLLAR_CONVERTER
    

def main():
  inputMessage = "Enter the number of days for which salary is to be computed(or press <Enter> to quit): "
  numOfDaysStr = input(inputMessage)
  numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr,inputMessage)
  
  while numOfDaysErrorCheckedInt:
    finalAmount = salaryCalculator(numOfDaysErrorCheckedInt)
    
    print("In ",numOfDaysErrorCheckedInt,"days a penny grows to $","{:.2f}".format(finalAmount))
    numOfDaysStr = input(inputMessage)
    numOfDaysErrorCheckedInt = errorCheck(numOfDaysStr, inputMessage)

  # tester1 = [4,14,30,365]
  # tester2 = [0.15,163.83,10737418.23,751533626487626648569070089221440991301881302634686635501610374244697292922233352950032061665551888458711040.00]
  # for testNum in range(len(tester1)):
  #   if salaryCalculator(tester1[testNum]) == tester2[testNum]:
  # 	  print("The program passed the test for the value ",tester1[testNum])
  #   else:
  #     print("The program did not pass the test")
    	

main()