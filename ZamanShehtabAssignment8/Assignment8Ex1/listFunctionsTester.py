#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 8: Problem 1
'''

Analysis

This program encrypts and decrypts messages using the caeser cipher method. 

Output to monitor:
  randomList(list) - The list being used for testing
  pythonSliceResult(list) - Slice of a list generated by python
  mySliceResult(list) - Slice of a list generated by function
  
Input from keyboard:
  startIndexInt - Index to start slicing from
  endIndexInt - Index to slice to (not including the index)

Tasks allocated to Functions:
  postiveintChecker(numStr) - checks if given string is positive 
  validIndexChekcer(list,startIndex,endingIndexStr) - checks if the indices 
    given are valid and usable in the function and return a runtime error 

  listEquivalenceChecker(givenListOne,givenListTwo) - given two lists checks
    if they are exactly the same. 
'''
import listFunctions

LIST_LENGTH = 20


# def mySlice(givenList, startIndex, endIndex):
#   resultList = []
#   for member in range(startIndex,endIndex):
#     resultList.append(givenList[member])
#   return resultList

def postiveintChecker(numStr):
  return numStr.isnumeric()

def validIndexChekcer(givenList,startingIndexStr, endingIndexStr):
  return int(startingIndexStr)<int(endingIndexStr) and int(endingIndexStr) <= len(givenList) 

def listEquivalenceChecker(givenListOne, givenListTwo):
  return givenListOne == givenListTwo

def main():
  randomList = listFunctions.generateRandomInts(LIST_LENGTH)
  print("The list is",randomList,"and its length is",len(randomList))

  startIndexStr = input("Enter the starting index for the slice\n\
  OR press <Enter> to quit: ")

  while startIndexStr:
    endIndexStr = input("Enter the limiting index for the slice: ")

    while not(postiveintChecker(startIndexStr) and postiveintChecker\
      (endIndexStr) and validIndexChekcer\
        (randomList,startIndexStr,endIndexStr)):
      print("One or both of your indices were invalid")
      startIndexStr = input("Enter the starting index for the slice: ")
      endIndexStr = input("Enter the limiting index for the slice: ")

    startIndexInt = int(startIndexStr)
    endIndexInt = int(endIndexStr)
    
    #print(randomList[startIndexInt:endIndexInt])
    #print(mySlice(randomList,startIndexInt,endIndexInt))
    pythonSliceResult = randomList[startIndexInt:endIndexInt]
    
    mySliceResult = listFunctions.listSlice(randomList,startIndexInt,endIndexInt)

    print("Python slice is:",pythonSliceResult)
    print("My Slice is:",mySliceResult)
    
    if listEquivalenceChecker(pythonSliceResult,mySliceResult):
      print("Success! The outputs match! \n")
    else:
      print("Oops something is went wrong!")

    

    startIndexStr = input("Enter the starting index for the slice \
      OR press <Enter> to quit: ")

main()