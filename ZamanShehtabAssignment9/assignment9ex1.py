#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 9: Problem 1

'''
Analysis

The purpose of this program is to calculate students averages and sort them
given a list of tuples containing names and grades where a name might appear
multiple times.

Output to monitor:
  table of name, number of scores and average. Once using dictionary method 
  and the other time using list of tuples method. 
  horizontalPrintLine() prints a horizontal line equal to the screen length  
  finalAmount (float) - The total salary after the given number of days.
 

Tasks allocated to Functions: 
  tupleListToDict(tupList)- returns a dictionary given a list of tuples. 
  sortedKeyList(unorderedDict) - given an unordered dictionary key returns 
                                a list of ordered keys. 
  computeAverage(gradeList) - given a list of ints averages them using 
                              running average method. 
  getSortedListOfTuples(listOfTuples)-given a list of tuples, orders them 
                                      according to the first index
  horizontalPrintLine() - returns a string that creates a dashed line on 
                          the monitor

'''
LINE_LENGTH = 35
#Returns a dictionary given a list of tuples
#param - List (of Tuples)
#return - dictionary
def tupleListToDict(tupList):
	resultDictionary = {}

	for key,vals in tupList:
		if key in resultDictionary:
			tempGradeList = resultDictionary[key]
		else:
			tempGradeList = []
		for grades in vals:
			tempGradeList.append(grades)
		resultDictionary[key] = tempGradeList
	return resultDictionary

#Returns an ordered list of dictionary keys
#param - dictionary
#return - list
def sortedKeyList(unorderedDict):
  ordereredList = list(unorderedDict.keys())
  ordereredList.sort()
  return ordereredList

#Given a list of ints creates an average of the elements
#param - List (of ints or floats)
#returns -float
def computeAverage(gradeList):
  total = 0.0
  average = 0.0
  for index in range(len(gradeList)):
    total += gradeList[index]
    
    #average calculated in loop so null list doesn't through an error
    average = total / (index+1)

  return average

#given a list of tuples, sorts them and returns a new list
#param - list (of tuples)
#returns - list
def getSortedListOfTuples(listOfTuples):
    newListOfTuples = list(listOfTuples)
    newListOfTuples.sort()
    return newListOfTuples
    
#parameter - none
#Draws a horizontal line in the the output screen according to the global
#constant LINE_LENGTH
def horizontalPrintLine():
  line = ""
  for dash in range(0,LINE_LENGTH):
    line +="-"
  return line

def main():
  gradeList = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]), \
  ('Slartibartfast',[]),('Trillian', [98, 88]), ('Trillian', [97, 77]),\
  ('Slartibartfast', []),('Marvin', [2000, 500]) , ('Arthur', [42, 20]),\
  ('Arthur', [64]),('Trillian', [99]), ('Marvin', [450]), ('Marvin', [550]),\
  ('Agrajag', []), ('Agrajag', []), ('Agrajag', [0]),\
  ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]
  
  dic = tupleListToDict(gradeList)
  
  #for key in dic:
  #  print(key,dic[key])
  
  orderedKeyList = sortedKeyList(dic)
  #print(orderedKeyLis)
  
  print("{0:20}{1:10}".format(" ","Grades"))
  print("{0:20} {1:5} {2:8}".format("Name","Count ","Average"))
  print(horizontalPrintLine())
  for key in orderedKeyList:
    #print(key,len(dic[key]),computeAverage(dic[key]))
    
    print("{0:20} {1:5} {2:8}".format(key,len(dic[key]),\
      computeAverage(dic[key])))
    
  
  listOfTuples = dic.items()
  
  orderedListOfTuples = getSortedListOfTuples(listOfTuples)

  print("\n")
  print("{0:20}{1:10}".format(" ","Grades"))
  print("{0:20} {1:5} {2:8}".format("Name","Count ","Average"))
  print(horizontalPrintLine())

  for name,grades in orderedListOfTuples:
    #print(name,computeAverage(grades))
    print("{0:20} {1:5} {2:8}".format(name,len(grades),\
      computeAverage(grades)))

main()