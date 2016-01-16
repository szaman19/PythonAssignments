'''
generateRandomInts(listSize) - creates a list with lenth listSize and 
  fills it with random ints
computeAverage(myList) - computes the average of the elements of the list
findMinValue(myLIst) - returns the smallest values of myList
findMaxValue(myLIst) - returns the largest values of myList
listSlice(givenList,startIndex,endIndex) - creates a new list with the
  elements from givenList between indices startIndex and endIndex

'''

import random

RANDOM_RANGE_UPPER_LIMIT = 1000
RANDOM_RANGE_LOWER_LIMIT = 0
INDEX_ZERO = 0
INDEX_ONE = 1
SUM_START_VALUE = 0

def generateRandomInts(listSize):
    
    myList = []
    for i in range(listSize):
        myList.append(random.randrange(RANDOM_RANGE_LOWER_LIMIT,\
            RANDOM_RANGE_UPPER_LIMIT))
    return myList

#computeSum(), computeAverage(), findMinValue(), and findMaxValue()
def computeSum(myList):
    sum = SUM_START_VALUE
    for member in myList:
        sum += member
    return sum

def computeAverage(myList):
    average = computeSum(myList)/len(myList)
    return average
    
def findMinValue(myList):
    currentMin = myList[INDEX_ZERO]
    for member in myList[INDEX_ONE:]:
        if currentMin > member:
            currentMin = member
    return currentMin
    
def findMaxValue(myList):
    currentMax = myList[INDEX_ZERO]
    for member in myList[INDEX_ONE:]:
        if currentMax < member:
            currentMax = member
    return currentMax

def listSlice(givenList, startIndex, endIndex):
  resultList = []
  for member in range(startIndex,endIndex):
    resultList.append(givenList[member])
  return resultList