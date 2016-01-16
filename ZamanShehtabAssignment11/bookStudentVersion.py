'''
Shehtab Zaman
szaman5@bignhamton.edu
B_55, NURI RA
Assignment 11
'''

'''
This class represents a book with a title, author, status,
a patron to whom the book is checked out, and a list
of patrons waiting for it
'''

class Book:

  # Class Variables ----------------------------------------------------------
  # index when book is first created (int)
  NONE = 0

  # index when book is loaned successfully (int)
  SUCCESSFUL = 1

  # index when patron is put on waiting list (int)
  WAIT = 2

  # index when request for loan is unsuccessful (int)
  UNSUCCESSFUL = 3

  # index when book is returned (int)
  RETURNED = 4

  # index when request for loan is invalid (int)
  INVALID = 5

  # status of most recent transaction with respect to this book (str)
  # Will be combined with name of patron participating in transaction and
  #   and title of this book"""
  TRANS_STATUS = [" No transactions yet",
                  " successfully checked out ",
                  " has been put on waiting list for ",
                  " must return books before taking out ",
                  " has returned ",
                  " has recorded an invalid transaction re:  "]

  # Constructor --------------------------------------------------------------

  # Creates a new book with the given title and author
  # params:  title (str) and author (str) of book
  # initialize:  self.__title (str) and self.__author (str) to value of
  #                incoming parameters
  #              self.__transactionStatus (str) to no transactions yet,
  #              self.__patron (Patron) & self.__waitList (list of Patrons)
  #                 to null/empty values
  def __init__(self, title, author):
    # your code here
    self.__title = title
    self.__author = author
    self.__transactionStatus = self.TRANS_STATUS[self.NONE]
    self.__waitList = list()
    self.__patron = None

  # Predicates ---------------------------------------------------------------

  # returns: True when book is already loaned out, False otherwise (bool)
  def isCheckedOut(self):
    # your code here
    return bool(self.__patron)

  # invokes len()
  # returns: True if Patron(s) are waiting for book, False otherwise (bool)
  def isReserved(self):
    # your code here
    return len(self.__waitList) > 0

  # params: patron - a particular patron (Patron)
  # returns: True when Patron has checked out book, False otherwise (bool)
  def hasBook(self, patron):
    # your code here
    return self.__patron == patron

  # params: patron - a particular patron (Patron)
  # returns: True when given Patron is on waiting list, False otherwise (bool)
  def isInWaitList(self, patron):
    # your code here
    return patron in self.__waitList

  # Both return and lend
  # returns: True when previous transaction is "returned" and current
  #            transaction is "lend", False otherwise (bool)
  def __isTwoPartStatus(self):
    # your code here
    return "return" in self.__transactionStatus and not "\n" in \
      self.__transactionStatus

  # Accessors ----------------------------------------------------------------

  # returns: title of book (str)
  def getTitle(self):
    # your code here
    return self.__title

  # returns: author of book (str)
  def getAuthor(self):
    # your code here
    return self.__author

  # returns: Patron who has checked out book (Patron)
  def getPatron(self):
    # your code here
    return self.__patron
  # returns: record of latest book transaction (str)
  def getTransactionStatus(self):
    # your code here
    return self.__transactionStatus

  # invokes: str()
  # returns: str representation of waiting list for book (str)
  def getWaitListStr(self):
    stringRep = ""
    for eachPatron in self.__waitList:
      stringRep += str(eachPatron) + " \n"
    return stringRep

    # your code here


  # Mutators -----------------------------------------------------------------

  # This method delegates all responsibilities to private methods of class
  # invokes: hasBook(), isInWaitList(), canCheckOutBooks(), isCheckedOut(),
  #          __lendBook(), __putInWaitList(), and __setTransactionStatus()
  # params:  patron - patron trying to borrow book (Patron)
  def borrowMe(self, patron):
    # your code here
    if not self.isCheckedOut():
        if patron.canCheckOutBooks():
            self.__lendBook(patron)
            self.__patron = patron
            self.__setTransactionStatus(patron.getName(),self.SUCCESSFUL)
        else:
            self.__setTransactionStatus(patron.getName(),\
            self.UNSUCCESSFUL)
    else:
        if self.hasBook(patron):
            self.__setTransactionStatus(patron.getName(),\
            self.INVALID)
        else:
            if self.isInWaitList(patron):
                self.__setTransactionStatus(patron.getName(),\
                self.INVALID)
            else:
                self.__putInWaitList(patron)
                self.__setTransactionStatus(patron.getName(),\
                self.WAIT)





  # Return book: release current patron, try to lend to waiting patron
  # This method delegates all responsibilities to private methods of class
  # invokes: isCheckedOut(), isReserved(), getName(),
  #          __resetPatron,(), __lendToNextPatron(), and
  #          __setTransactionStatus()
  def returnMe(self): # mutator controller
    # your code here
    if self.isCheckedOut():
        self.__resetPatron()
        self.__setTransactionStatus(self.__patron.getName()\
        ,self.RETURNED)
    if self.isReserved():
        self.__lendToNextPatron()
    else:
        self.__patron = None



  def __lendBook(self, patron):
    # your code here

    patron.increment()


  # invokes: decrement() (Patron class)
  def __resetPatron(self):
    # your code here
    self.__patron.decrement()
    #self.__patron = None

  # Lend book to waiting patron if eligible; if not, remove from wait List
  # invokes: isCheckedOut(), isReserved(),
  #          pop() (from list), borrowMe()
  def __lendToNextPatron(self): # waitList mutator
    # your code here
    if self.isReserved():
        temp = self.__waitList.pop(0)
        #print("_________________________________________")
        #print(temp)
        #print("_________________________________________")
        self.__patron = None
        self.borrowMe(temp)
        #print(self.__patron)
        #print("_________________________________________")



  # params:  patron - Patron to put in waiting list (Patron)
  # invokes: append() (to list)
  def __putInWaitList(self, patron): # waitList mutator
    # your code here
    self.__waitList.append(patron)

  # Creates string describing latest transaction
  # Combines name of patron participation in transaction with
  #   status of most recent transaction and title of this book
  # params: name - name of Patron participating in transaction (str)
  #         index - index of transaction in TRANS_STATUS (int)
  # invokes: __isTwoPartStatus()
  def __setTransactionStatus(self, name, index):# transStatus mutator
    # your code here
    if self.__isTwoPartStatus():
      self.__transactionStatus += "\n"
    else:
      self.__transactionStatus = ""
    self.__transactionStatus += name+self.TRANS_STATUS[index]\
    +self.__title

  # Comparators --------------------------------------------------------------

  # Already written for you:
  # Include these in order to sort Book objects


  # Shows how two Books can be compared with respect to the < relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when they are not same Book and other is Book object and
  #            title of this Book is lexicographically lower than title of
  #            other Book, False otherwise (bool)"""
  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__title < other.__title

  # Shows how two Books can be compared with respect to the == relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when both are same Book or both are Book objects and
  #            title and author are equal, False otherwise (bool)
  def __eq__(self, other):
    return self is other or \
           (type(self) == type(other) and \
            self.__title == other.__title) and\
            self.__author == other.__author

  # Convert to Str -----------------------------------------------------------

  # invokes:  str(), getWaitListStr()
  # returns:  str representation of Book object (str)
  def __str__(self):
    # your code here
    checkedOutString = ""
    if self.isCheckedOut():
        checkedOutString = "Checked out" + str(self.__patron) +"\n"
    else:
        checkedOutString = "Not checked out" +"\n"


    return "Title: " + self.__title+"\n"\
    "Author: " + self.__author+"\n"\
    +checkedOutString\
    +"WaitList : \n" + self.getWaitListStr() + "\n"
