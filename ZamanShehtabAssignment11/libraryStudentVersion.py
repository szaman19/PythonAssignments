'''
Shehtab Zaman
szaman5@bignhamton.edu
B_55, NURI RA
Assignment 11
'''

from libraryModule import StringGeneratorForDictionaries

'''
This class represents a named library with books and patrons.
A library can add and remove Patrons, add and remove Books,
access information about its Patrons and Books, and keep track of
any transactions taking place with repect to it's Books and Patrons.
This class makes use of the StringGeneratorForDictionaries class found
in the libraryModule file.
'''
class Library:

#-- Class Variables ----------------------------------------------------

  # Index when book not in library
  NOT_IN_LIBRARY = 0

  # Index when book added to library
  ADD = 1

  # Index when book removed from library
  REMOVE = 2

  # Index when patron not a member of library
  NOT_A_MEMBER = 3

  # Index when patron becomes member of library
  JOIN = 4

  # Index when patron ends membership in library
  LEAVE = 5

  # Index when book information is accessed
  ACCESS = 6

  # Index when patron information is accessed
  LOOK_UP = 7

  # Most recent transaction with respect to either a book or a patron
  TRANS_STATUS = [" is not in library",
                  " has been added to the library",
                  " has been removed from the library ",
                  " is not a library member ",
                  " has been added as a library member",
                  " has been removed as a library member",
                  " has been accessed",
                  " member files have been accessed"]

#-- Constructor --------------------------------------------------------

  # Creates new dictionaries to hold books and patrons
  # params:  name - name of Library(str)
  # initialize:  self.__name (str), to parameter name,
  #              self.__books (dict of Book)  and
  #              self.__patrons() (dict of Patron) to empty dictionaries,
  #              self.__transactionStatus (str) to TRANS_STATUS with respect to
  #                book participating in transaction or
  #                patron participating in transaction
  def __init__(self, name):
    # your code here
    self.__name = name
    self.__books = {}
    self.__patrons = {}
    self.__transactionStatus = ""

#-- Accessors ----------------------------------------------------------

  # returns:  name of library (str)
  def getName(self):
    # your code here
    return self.__name


  # returns:  record of latest transaction (str)
  def getTransactionStatus(self):
    # your code here
    return self.__transactionStatus

  # params:  title of Book (str)
  # invokes:  inLibrary(), __setTransactionStatus()
  # returns:  Book stored in library (Book)
  def getBook(self, title):
    # your code here
    tempBook = ""
    if self.inLibrary(title):
      tempBook = self.__books[title]
      self.__setTransactionStatus(title,"",\
      self.ACCESS)
    else:
      self.__setTransactionStatus(title,"",\
      self.NOT_IN_LIBRARY)
    return tempBook




  # params: name of Patron who is member of library (str)
  # invokes:  isMember(),  __setTransactionStatus()
  # returns:  name of Patron (Patron) or None
  def getPatron(self, name):
    # your code here
    tempMember = None
    if self.isMember(name):
        tempMember = self.__patrons[name]
        self.__setTransactionStatus\
        ("",name,self.LOOK_UP)
    else:
        self.__setTransactionStatus\
        ("",name,self.NOT_A_MEMBER)
    return tempMember


#-- Predicates ---------------------------------------------------------

  # Checks if book is in library
  # params: title - title of Book to search for in library (str)
  # returns:  True if in library, False otherwise (bool)
  def inLibrary(self, title):
    # your code here
    return title in self.__books

  # Checks if person is member of library
  # params: name - name of Patron to search for in library (str)
  # returns:  True if member of library, False otherwise (bool)
  def isMember(self, patronName):
    # your code here
    return patronName in self.__patrons

  # Checks if library has any books
  # invokes:  len()
  # returns:  True if library has any books, False otherwise (bool)
  def hasBooks(self):
    # your code here
    return len(self.__books.keys()) > 0

  # Checks if library has any members
  # invokes:  len()
  # returns:  True if library has any members, False otherwise (bool)
  def hasMembers(self):
    # your code here
    return len(self.__patrons.keys())>0


#-- Mutators -----------------------------------------------------------

  # Set status for latest transaction
  # params:  title - title of Book participating in transaction (str)
  #          name = name of Patron participating in transaction (str)
  #          Note:  one of the above should be an empty string
  #          index into TRANS_STATUS (int)
  def __setTransactionStatus(self, title, name, index):
    # your code here
    #print("Working on it")
    return title + name + self.TRANS_STATUS[index]

  # Adds book to library using its title as a key
  # params:  book - new Book to be added to library (Book)
  # invokes:  getTitle() (Book), __setTransactionStatus()
  def addBook(self, book):
    # your code here
    self.__books[book.getTitle()] = book

  # Removes book from library and releases borrower if applicable
  # params:  title - title of Book to remove from library (str)
  # invokes:  pop() (list),
  #           isCheckedOut() (Book), getPatron (Book)
  #           decrement () (Patron)
  #           inLibrary(), __setTransactionStatus()
  def removeBook(self, title):
    # your code here
    if self.inLibrary(title):
        tempBook = self.getBook(title)
        if tempBook.isCheckedOut():
            tempPatron = tempBook.getPatron()
            tempPatron.decrement()
        self.__books.pop(title)
        self.__setTransactionStatus(title,"",self.REMOVE)



  # Adds patron to library using its name as a key
  # params:  patron - new Patron to add to library (Patron)
  # invokes:  getName (Patron), __setTransactionStatus()
  def addPatron(self, patron):
    # your code here
    self.__patrons[patron.getName()] = patron

  # Removes the patron and returns borrowed books if any
  # params:  name - name of Patron to remove from library (str)
  # invokes:  pop() (list),
  #           hasCheckedOutBooks() (Patron)
  #           getPatron (Book), returnMe (Book)
  #           isMember(), __setTransactionStatus()
  def removePatron(self, name):
    # your code her
    if self.isMember(name):
        temp = self.getPatron(name)
        if temp.hasCheckedOutBooks():
            for each in self.__books:
                tempBook = self.__books[each]
                if temp == tempBook.getPatron():
                    tempBook.returnMe()
        self.__patrons.pop(name)
        self.__setTransactionStatus("",name,self.LEAVE)

#-- Convert to Str -----------------------------------------------------

  # Generates string representation of library
  # creates:  StringGeneratorForDictionaries objects
  # invokes:  str(), getName(), hasBooks(), hasMembers(),
  #           getDictString() (StringGeneratorForDictionaries)
  # returns:  str representation of Library object (str)
  def __str__(self):
      books = ""
      if self.hasBooks():
          books = "Books: \n"
          for eachBook in self.__books:
              books+= self.__books[eachBook]\
              .getTitle()+": \n" +\
              str(self.__books[eachBook]) + "\n"
      else:
          books = "There are no books in the Library"
      members = ""
      if self.hasMembers():
          members = "Patrons: \n"
          for eachMember in self.__patrons:
              members += str(self.__patrons[eachMember])+"\n"
      else:
          members = "There are no members in the Library"
      return self.__name+": \n" + books + members
