'''
Rose Williams
'''

'''
This program finds the population of a city via database query
Output:
  query result (str)
Input:
  city (str)
Classes Used:
  BadArgument
  QueryWorldBD
'''

import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):

#-- Constructor --------------------------------------------------------

  def __init__(self):
    self.__title = 'Missing Argument'
    self.__message = 'Population given out of range contains invalid characters'

#-- Accessors ----------------------------------------------------------

  # return title (str)
  def getTitle(self):
    return self.__title

#-- to String ----------------------------------------------------------

  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDB:

  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, dBName):
    conn = sqlite3.connect(dBName)
    self.__cursor = conn.cursor()
    # Must make city instance variable so that it is accessible to all methods
    self.__minPopulation = ""
    self.__maxPopulation = ""
    self.__listOfCities = None


  def __isValidRange(self,population):
    self.__cursor.execute("SELECT min(population) FROM city")
    absMin = self.__cursor.fetchone()[0]

    self.__cursor.execute("SELECT max(population) FROM city")
    absMax = self.__cursor.fetchone()[0]
    return int(population) >= absMin and int(population) <= absMax
# -- Mutators ----------------------------------------------------------------

  #
  # param cityName (str)
  def setPop(self, minPop, maxPop):
    self.__minPopulation = minPop
    self.__maxPopulation = maxPop


  # raises BadArgument Exception if city is blank or contains invalid chars
  # def popQuery(self):
  #   if self.__currentCity.replace('_','A').isalpha():
  #     self.__cursor.execute('select population from city where name = ?',\
  #                         (self.__currentCity,))
  #   else:
  #     raise BadArgument()


  def popQuery(self):
    if self.__isValidRange(self.__minPopulation) and self.__isValidRange(self.__maxPopulation):
      self.__cursor.execute('select name,population from city where population >= ? and population <= ? order by population',\
                          (self.__minPopulation,self.__maxPopulation))
    else:
      raise BadArgument()


  # Close connection to db
  def closeConnection(self):
    self.__cursor.close()


# -- toString ----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    # Note that if city isn't in database, then answer will be None
    # If city is in database, answer will be a tuple object
    # Will have to get element[0] of tuple in order to use it
    self.__listOfCities = self.__cursor.fetchall()
    string = ""
    if self.__listOfCities:
      for element in self.__listOfCities:
        string += element[0] +" has a Population of : "\
        +str(element[1]) +"\n"
    else:
      string = "There are no cities in that range"
    return string
    # Note that 4th format specifier denotes a string rather than an int in
    # order to accommodate possibility that answer is None
    # return '%s %s %s %s\n' % (
    #   ('The population of' if answer else 'There is no city named'),
    #   self.__currentCity,
    #   ('is' if answer else 'in the database'),
    #   ('' if answer == None else str(answer[0])) )

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Find population of any city stored in world database
# Cities must contain only alphabetic characters with the exeception of mult-
#   word cities, which must be connected with '_' (no spaces allowed)
def main():
  # set up connection and create cursor
  query = QueryWorldDB('worldDB')

  print("Find the vity by population \n")

  # get input from user (priming read)
  populationMin = input("Enter the min population, "+\
               "(Press <Enter> to quit):  ")

  populationMax = input("Enter the max population, "+\
               "(Press <Enter> to quit):  ")

  # let user get as many results as desired
  while populationMin and populationMax:
    try:
      # set up and issue query
      query.setPop(populationMin,populationMax)
      query.popQuery()
      # show results
      print(query)
    except BadArgument as err:
      # city input empty or malformed
      print('\n%s: %s\n' % (err.getTitle(), str(err) ))

    # let user enter another city (continuation read)
    print("Find the City by population \n")

    # get input from user (priming read)
    populationMin = input("Enter the min population, "+\
                 "(Press <Enter> to quit):  ")

    populationMax = input("Enter the max population, "+\
                 "(Press <Enter> to quit):  ")

  # close connection to db
  query.closeConnection()

main()
