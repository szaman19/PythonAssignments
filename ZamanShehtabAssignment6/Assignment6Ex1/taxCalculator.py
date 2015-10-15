#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 6: Problem 1

'''
The assignment goal was to create a program that is able to calculate the taxes
according to the graduated tax model using nested and chained conditionals.

The program takes in the marital status and total taxable income.

Functions used are:
  isMarried(statusString) -> Predicate function checks whether married or
                             not.
  percentCalculator(amount, nPercent) -> Returns n percent of the given amount.
  computeTax(statusString, taxedIncome) -> Computes the tax, given the marital
                                           status and income. 

'''

MARRIED_TAX_BRACKET_ONE = 18150
MARRIED_TAX_BRACKET_TWO= 73500
MARRIED_TAX_BRACKET_THREE = 148850
MARRIED_TAX_BRACKET_FOUR = 226850
MARRIED_TAX_BRACKET_FIVE = 405110
MARRIED_TAX_BRACKET_SIX = 457500

MARRIED_BRACKET_ONE_BASE = 0
MARRIED_BRACKET_TWO_BASE = 1815
MARRIED_BRACKET_THREE_BASE = 10162.5
MARRIED_BRACKET_FOUR_BASE = 28925
MARRIED_BRACKET_FIVE_BASE = 50765
MARRIED_BRACKET_SIX_BASE = 109587.5
MARRIED_BRACKET_SEVEN_BASE = 127962.5

SINGLE_TAX_BRACKET_ONE = 9075
SINGLE_TAX_BRACKET_TWO = 36900
SINGLE_TAX_BRACKET_THREE = 89350
SINGLE_TAX_BRACKET_FOUR = 186350
SINGLE_TAX_BRACKET_FIVE = 405100
SINGLE_TAX_BRACKET_SIX = 406750

SINGLE_BRACKET_ONE_BASE = 0
SINGLE_BRACKET_TWO_BASE = 907.5
SINGLE_BRACKET_THREE_BASE = 5081.25
SINGLE_BRACKET_FOUR_BASE = 18193.75
SINGLE_BRACKET_FIVE_BASE = 45353.75
SINGLE_BRACKET_SIX_BASE = 117541.25
SINGLE_BRACKET_SEVEN_BASE = 118118.75

BRACKET_ONE_RATE = 10
BRACKET_TWO_RATE = 15
BRACKET_THREE_RATE = 25
BRACKET_FOUR_RATE = 28
BRACKET_FIVE_RATE = 33
BRACKET_SIX_RATE = 35
BRACKET_SEVEN_RATE = 39.6

#One param (string)
#Checks whether married or not 
#Returns bool
def isMarried(statusString):
  lowerStatusString = statusString.lower()
  return (lowerStatusString == 'married')
#Two Params
#Returns percent value of an amount given and rate given
#Returns float
def percentCalculator(amount, nPercent):
  cent = 100
  nPercentAmount = ((amount / cent)*nPercent)
  return nPercentAmount

#Two Params (stirng, int)
#Given marital status and taxed income, computes total tax
#Returns float 
def computeTax(statusString, taxedIncome):
  totalTax = 0
  
  if(isMarried(statusString)):
    if( taxedIncome <= MARRIED_TAX_BRACKET_ONE):
      totalTax = percentCalculator(taxedIncome, BRACKET_ONE_RATE)
      
    elif(taxedIncome <= MARRIED_TAX_BRACKET_TWO):
      totalTax = MARRIED_BRACKET_TWO_BASE + percentCalculator\
                 (taxedIncome-MARRIED_TAX_BRACKET_ONE,BRACKET_TWO_RATE)
      
    elif(taxedIncome <= MARRIED_TAX_BRACKET_THREE):
      totalTax = MARRIED_BRACKET_THREE_BASE + percentCalculator\
                 (taxedIncome-MARRIED_TAX_BRACKET_TWO,BRACKET_THREE_RATE)
      
    elif(taxedIncome <= MARRIED_TAX_BRACKET_FOUR):
      totalTax = MARRIED_BRACKET_FOUR_BASE + percentCalculator\
                 (taxedIncome-MARRIED_TAX_BRACKET_THREE,BRACKET_FOUR_RATE)
      
    elif(taxedIncome <= MARRIED_TAX_BRACKET_FIVE):
      totalTax = MARRIED_BRACKET_FIVE_BASE + percentCalculator\
                 (taxedIncome-MARRIED_TAX_BRACKET_FOUR,BRACKET_FIVE_RATE)
      
    elif(taxedIncome <= MARRIED_TAX_BRACKET_SIX):
      totalTax = MARRIED_BRACKET_SIX_BASE + percentCalculator\
                 (taxedIncome-MARRIED_TAX_BRACKET_FIVE,BRACKET_SIX_RATE)
    else:
      totalTax = MARRIED_BRACKET_SEVEN_BASE + percentCalculator\
                 (taxedIncome-MARRIED_TAX_BRACKET_SIX,BRACKET_SEVEN_RATE)
      
  else:
    if(taxedIncome <= SINGLE_TAX_BRACKET_ONE):
      totalTax = percentCalculator(taxedIncome, BRACKET_ONE_RATE)
    
    elif(taxedIncome <= SINGLE_TAX_BRACKET_TWO):
      totalTax = SINGLE_BRACKET_TWO_BASE + percentCalculator\
                 (taxedIncome-SINGLE_TAX_BRACKET_ONE,BRACKET_TWO_RATE)
      
    elif(taxedIncome <= SINGLE_TAX_BRACKET_THREE):
      totalTax = SINGLE_BRACKET_THREE_BASE + percentCalculator\
                 (taxedIncome-SINGLE_TAX_BRACKET_TWO,BRACKET_THREE_RATE)
      
    elif(taxedIncome <= SINGLE_TAX_BRACKET_FOUR):
      totalTax = SINGLE_BRACKET_FOUR_BASE + percentCalculator\
                 (taxedIncome-SINGLE_TAX_BRACKET_THREE,BRACKET_FOUR_RATE)
      
    elif(taxedIncome <= SINGLE_TAX_BRACKET_FIVE):
      totalTax = SINGLE_BRACKET_FIVE_BASE + percentCalculator\
                 (taxedIncome-SINGLE_TAX_BRACKET_FOUR,BRACKET_FIVE_RATE)
      
    elif(taxedIncome <= SINGLE_TAX_BRACKET_SIX):
      totalTax = SINGLE_BRACKET_SIX_BASE + percentCalculator\
                 (taxedIncome-SINGLE_TAX_BRACKET_FIVE,BRACKET_SIX_RATE)
      
    else:
      totalTax = SINGLE_BRACKET_SEVEN_BASE + percentCalculator\
                 (taxedIncome-SINGLE_TAX_BRACKET_SIX,BRACKET_SEVEN_RATE)
      
  return totalTax

#One param
#Checks if status string is married or single
#Returns bool 
def errorCheckMaritalStatus(maritalStatusString):
  return maritalStatusString.lower()=="married" \
  or maritalStatusString.lower()=="single"
#One param 
#Checks if string can be changed to float and >0
#Returns false or float 
def errorCheckTaxableIncome(taxableIncomeString):
  try:
    floatResult = float(taxableIncomeString)
  except ValueError:
    floatResult = False
  return floatResult < 0 or floatResult

  
#Asks user for marital status and then income, checks if input is valid 
#and outputs status, income, and tax  
def main():
  #Priming read 
  maritalStatus = input("What is your marital status? or <Enter to quit>")

  #Continuation loop
  while maritalStatus:
    
    #Validation loop - marital status
    while not errorCheckMaritalStatus(maritalStatus):
      print("Invalid marital status: Use single or married")
      maritalStatus = input("What is your marital status? or <Enter to quit>")
        
    taxableIncome = input("What is your taxable income? ")
    
    errorCheckedTaxableIncome = errorCheckTaxableIncome(taxableIncome)

    #Validation loop- taxable Income
    while not errorCheckedTaxableIncome:
      print("Invalid income. Use number greater than 0")
      taxableIncome = input("What is your taxable income? ")
      errorCheckedTaxableIncome = errorCheckTaxableIncome(taxableIncome)
    
    #Tax output 
    print("%s, $%.2f = $%.2f" % \
     (maritalStatus,errorCheckedTaxableIncome,\
      computeTax(maritalStatus,errorCheckedTaxableIncome))) 
    print('\n')
    
    #Continuation read 
    maritalStatus = input("What is your marital status? or <Enter to quit>")

  
  
  # states = ['single', 'married']

  # incomes = [[0,9075, 9076, 36900, 36901, 89350, 89351,

  #             186350, 186351, 405100, 405101, 406750, 406751],

  #            [0, 18150, 18151, 73800, 73801, 148850, 148851,

  #            226850, 226851,  405100, 405101, 457600, 457601]]

  # for i in range(len(states)):

  #   for j in range(len(incomes[0])):

  #     print("%s, $%.2f = $%.2f" % (states[i], incomes[i][j], computeTax(states[i], incomes[i][j])))


  
  
main()
