'''
Shehtab Zaman
szaman5@bignhamton.edu
B_55, NURI RA
Assignment 11
'''
import tkinter as Tk
import tkinter.messagebox

from patronStudentVersion import *
from bookStudentVersion import *
from libraryStudentVersion import *
'''
This class creates a gui that allows the user to add remove
patrons, add/remove books, and check out and return books.

It uses tkinter, patronStudentVersion, bookStudentVersion and
libraryStudentVersion classes. 
'''

ROW_ZERO = 0
ROW_ONE = 1
ROW_TWO = 2
ROW_THREE = 3
ROW_FOUR = 4
ROW_FIVE = 5
ROW_SIX = 6
ROW_SEVEN = 7
ROW_EIGHT = 8
ROW_NINE = 9
ROW_TEN = 10
ROW_ELEVEN = 11
ROW_TWELVE= 12
ROW_THIRTEEN= 13
ROW_FOURTEEN= 14
ROW_FIFTEEN= 15
ROW_SIXTEEN= 16
ROW_SEVENTEEN= 17
ROW_EIGHTEEN= 18
ROW_NINETEEN=19

COL_ONE=1
COL_TWO=2
COL_THREE=3
COL_FOUR=4
COL_FIVE=5

WIDTH = 50

PADDING_TEN = 10
PADDING_FIFTEEN = 15
PADDING_TWENTY_FIVE= 25
PADDING_SIXTY = 60
PADDING_FORTY = 40

class LibraryGridGUI:
    def __init__(self):
        self.__win = Tk.Tk()
        self.__win.title('Megadodo Publications Library ')

        self.__libraryModel = Library("Megadodo Publications")

        self.__libraryLabel = Tk.Label\
        (self.__win,text="LIBRARY")

        self.__cbLabel = Tk.Label\
        (self.__win,text="Checkout Books")
            #Return Books Label
        self.__rbLabel = Tk.Label\
        (self.__win,text="Return Books")
            #Book Label
        self.__bLabel = Tk.Label\
        (self.__win,text="Book")
            #Patron Label
        self.__pLabel = Tk.Label\
        (self.__win, text="Patron")
            #Join Label
        self.__jLabel = Tk.Label\
        (self.__win,text="Join")
            #Leave Label
        self.__lLabel = Tk.Label\
        (self.__win, text="Leave")
            #
        self.__membershipLabel = Tk.Label\
        (self.__win,text="MEMBERSHIP", relief=Tk.GROOVE)
            #
        self.__collectionLabel = Tk.Label\
        (self.__win, text="BOOK COLLECTION", relief=Tk.GROOVE)
            #
        self.__entryOneLabel = Tk.Label\
        (self.__win, text="Title: ")

        self.__entryOne = Tk.Entry\
        (self.__win,width=WIDTH)

        #self.__entryOne.bind('<Return>',self.set)
            #
        self.__entryTwoLabel = Tk.Label\
        (self.__win, text="Title: ")

        self.__entryTwo = Tk.Entry\
        (self.__win,width=WIDTH)
            #
        self.__entryThreeLabel = Tk.Label\
        (self.__win, text="Patron: ")

        self.__entryThree = Tk.Entry\
        (self.__win,width=WIDTH)
            #
        self.__entryFourLabel = Tk.Label\
        (self.__win, text="Patron")
            #
        self.__cbButton = Tk.Button\
        (self.__win,text="Checkout Book",command = self.__checkOutBook)

        self.__rbButton = Tk.Button\
        (self.__win,text="Return Book",command = self.__returnBook)

        self.__abButton = Tk.Button\
        (self.__win,text = "Add Book",command = self.__addBook)

        self.__rmButton = Tk.Button\
        (self.__win, text = "Remove Book", command = self.__removeBook)

        self.__exitButton = Tk.Button(self.__win,\
        text = "Exit", command=self.exit)

        self.__dyLabel1 = Tk.Label\
        (self.__win,text="Status: ")

        self.__dyLabel2 = Tk.Label\
        (self.__win,text="Status: ")

        self.__checkoutTransStatus = Tk.StringVar()

        self.__checkoutTransStatus.set("No transaction")

        self.__checkOutStatus = Tk.Label(self.__win,\
        textvariable=self.__checkoutTransStatus)

        self.__returnBookTransStatus = Tk.StringVar()

        self.__returnBookTransStatus.set("No transaction")

        self.__returnBookStatus = Tk.Label(self.__win,\
        textvariable=self.__returnBookTransStatus)

        self.__searchLabel = Tk.Label\
        (self.__win,text="SEARCH", relief=Tk.GROOVE)

        self.__bookLabel = Tk.Label\
        (self.__win,text="Title: ")

        self.__entryFive = Tk.Entry\
        (self.__win,width=WIDTH)

        self.__entryFive.bind("<Return>", self.__searchBook)

        self.__patronLabel = Tk.Label\
        (self.__win,text="Name")

        self.__entrySix = Tk.Entry\
        (self.__win,width=WIDTH)
        self.__entrySix.bind("<Return>",self.__searchPatron)

        self.__dyLabel3 = Tk.Label\
        (self.__win,text="Status: ")

        self.__dyLabel4 = Tk.Label\
        (self.__win,text="Status: ")

        self.__bookSearchStatus = Tk.StringVar()

        self.__bookSearchStatus.set("No transaction")
        self.__bookStatus = Tk.Label(self.__win,\
        textvariable=self.__bookSearchStatus)

        self.__patronSearchStatus = Tk.StringVar()

        self.__patronSearchStatus.set("No transaction")
        self.__patronStatus = Tk.Label(self.__win,\
        textvariable=self.__patronSearchStatus)

        self.__joinLabel = Tk.Label\
        (self.__win,text="Name: ")

        self.__entrySeven = Tk.Entry\
        (self.__win,width=WIDTH)

        self.__entrySeven.bind("<Return>",self.__joinLibrary)

        self.__leaveLabel = Tk.Label\
        (self.__win,text="Name: ")

        self.__entryEight = Tk.Entry\
        (self.__win,width=WIDTH)

        self.__entryEight.bind("<Return>",self.__leaveLibrary)

        self.__dyLabel5 = Tk.Label\
        (self.__win,text="Status: ")

        self.__dyLabel6 = Tk.Label\
        (self.__win,text="Status: ")

        self.__patronJoinStatus = Tk.StringVar()
        self.__patronJoinStatus.set("No transaction")

        self.__joinStatus = Tk.Label(self.__win,\
        textvariable=self.__patronJoinStatus)

        self.__patronLeaveStatus = Tk.StringVar()
        self.__patronLeaveStatus.set("No transaction")

        self.__leaveStatus = Tk.Label(self.__win,\
        textvariable=self.__patronLeaveStatus)

        self.__entryNineLabel=Tk.Label\
        (self.__win,text="Title: ")

        self.__entryNine = Tk.Entry\
        (self.__win,width=WIDTH)

        self.__entryTenLabel = Tk.Label\
        (self.__win,text="Author: ")

        self.__entryTen = Tk.Entry\
        (self.__win,width=WIDTH)

        self.__entryElevenLabel = Tk.Label\
        (self.__win,text="Title: ")

        self.__entryEleven = Tk.Entry\
        (self.__win,width=WIDTH)

        self.__entryTwelveLabel = Tk.Label\
        (self.__win,text="Author: ")

        self.__dyLabel7 = Tk.Label\
        (self.__win,text="Status: ")

        self.__dyLabel8 = Tk.Label\
        (self.__win,text="Status: ")

        self.__addBookStatus = Tk.StringVar()
        self.__addBookStatus.set("No transaction")
        self.__addBook = Tk.Label(self.__win,\
        textvariable=self.__addBookStatus)

        self.__removeBookStatus = Tk.StringVar()
        self.__removeBookStatus.set("No transaction")
        self.__removeBook = Tk.Label(self.__win,\
        textvariable=self.__removeBookStatus)
#________________________________________________________________________#
#___________________________________GRIDS________________________________#
        self.__libraryLabel.grid(row=ROW_ZERO,column=COL_THREE,\
        pady=PADDING_FIFTEEN)
        self.__cbLabel.grid(row=ROW_ONE,column=COL_TWO)
        self.__rbLabel.grid(row=ROW_ONE,column=COL_FOUR)

        self.__entryOneLabel.grid(row=ROW_TWO,column=COL_ONE)
        self.__entryOne.grid(row=ROW_TWO,column=COL_TWO)

        self.__entryTwoLabel.grid(row=ROW_TWO,column=COL_THREE)
        self.__entryTwo.grid(row=ROW_TWO,column=COL_FOUR)

        self.__entryThreeLabel.grid(row=ROW_THREE,column=COL_ONE)
        self.__entryThree.grid(row=ROW_THREE,column=COL_TWO)

        self.__entryFourLabel.grid(row=ROW_THREE, column=COL_THREE)

        self.__cbButton.grid(row=ROW_FOUR,column=COL_TWO)
        self.__rbButton.grid(row=ROW_FOUR,column=COL_FOUR)

        self.__dyLabel1.grid(row=ROW_FIVE,column=COL_ONE)
        self.__checkOutStatus.grid(row=ROW_FIVE,column=COL_TWO)
        self.__dyLabel2.grid(row=ROW_FIVE,column=COL_THREE)
        self.__returnBookStatus.grid(row=ROW_FIVE,column=COL_FOUR)

        self.__searchLabel.grid(row=ROW_SIX,column=COL_THREE,\
        pady=PADDING_FIFTEEN, ipadx=PADDING_SIXTY)

        self.__bLabel.grid(row=ROW_SEVEN,column=COL_TWO)
        self.__pLabel.grid(row=ROW_SEVEN,column=COL_FOUR)

        self.__bookLabel.grid(row=ROW_EIGHT,column=COL_ONE)
        self.__entryFive.grid(row=ROW_EIGHT,column=COL_TWO)
        self.__patronLabel.grid(row=ROW_EIGHT,column=COL_THREE)
        self.__entrySix.grid(row=ROW_EIGHT,column=COL_FOUR)

        self.__dyLabel3.grid(row=ROW_NINE,column=COL_ONE)
        self.__bookStatus.grid(row=ROW_NINE,column=COL_TWO)
        self.__dyLabel4.grid(row=ROW_NINE,column=COL_THREE)
        self.__patronStatus.grid(row=ROW_NINE,column=COL_FOUR)

        self.__membershipLabel.grid(row=ROW_TEN,column=COL_THREE,\
        pady=PADDING_FIFTEEN, ipadx=PADDING_FORTY)

        self.__jLabel.grid(row=ROW_ELEVEN,column=COL_TWO)
        self.__lLabel.grid(row=ROW_ELEVEN,column=COL_FOUR)

        self.__joinLabel.grid(row=ROW_TWELVE,column=COL_ONE)
        self.__entrySeven.grid(row=ROW_TWELVE,column=COL_TWO)
        self.__leaveLabel.grid(row=ROW_TWELVE,column=COL_THREE)
        self.__entryEight.grid(row=ROW_TWELVE,column=COL_FOUR)

        self.__dyLabel5.grid(row=ROW_THIRTEEN,column=COL_ONE)
        self.__joinStatus.grid(row=ROW_THIRTEEN,column=COL_TWO)
        self.__dyLabel6.grid(row=ROW_THIRTEEN,column=COL_THREE)
        self.__leaveStatus.grid(row=ROW_THIRTEEN,column=COL_FOUR)

        self.__collectionLabel.grid(row=ROW_FOURTEEN,column=COL_THREE,\
        pady=PADDING_FIFTEEN,ipadx=PADDING_FORTY)

        self.__entryNineLabel.grid(row=ROW_FIFTEEN,column=COL_ONE)
        self.__entryNine.grid(row=ROW_FIFTEEN,column=COL_TWO)

        self.__entryElevenLabel.grid(row=ROW_FIFTEEN,column=COL_THREE)
        self.__entryEleven.grid(row=ROW_FIFTEEN,column=COL_FOUR)

        self.__entryTenLabel.grid(row=ROW_SIXTEEN,column=COL_ONE)
        self.__entryTen.grid(row=ROW_SIXTEEN,column=COL_TWO)

        self.__entryTwelveLabel.grid(row=ROW_SIXTEEN,column=COL_THREE)

        self.__abButton.grid(row=ROW_SEVENTEEN,column=COL_TWO)
        self.__rmButton.grid(row=ROW_SEVENTEEN,column=COL_FOUR)

        self.__dyLabel7.grid(row=ROW_EIGHTEEN,column=COL_ONE)
        self.__addBook.grid(row=ROW_EIGHTEEN,column=COL_TWO)
        self.__dyLabel8.grid(row=ROW_EIGHTEEN,column=COL_THREE)
        self.__removeBook.grid(row=ROW_EIGHTEEN,column=COL_FOUR)

        self.__exitButton.grid(row=ROW_NINETEEN,column=COL_FOUR,sticky="E",\
        ipadx=PADDING_TWENTY_FIVE,padx=PADDING_TEN,pady=PADDING_FIFTEEN)


        Tk.mainloop()

    def exit(self):
        self.__win.destroy()

    #Clear All other labels
    # def __updateDisplay(self):
    #
    #     print("working on this")

    #Check out books
    #Called after clicking Button
    def __checkOutBook(self):
        bookTitle = self.__entryOne.get()
        bookPatron = self.__entryThree.get()
        #print(bookTitle,bookPatron)
        if(bookTitle and bookPatron):
            chosenBook = self.__libraryModel.getBook(bookTitle)
            member = self.__libraryModel.getPatron(bookPatron)
            if chosenBook and member:
                chosenBook.borrowMe(member)
            #print(self.__libraryModel.getTransactionStatus())
            #print(chosenBook.getTransactionStatus())
                string = chosenBook.getTransactionStatus()
                self.__checkoutTransStatus.set(string)
            else:
                transStr = self.__libraryModel.getTransactionStatus()
                self.__checkoutTransStatus.set(transStr)
                #chosenBook.getTransactionStatus()

    #Return book
    #Called after clicking return book button
    def __returnBook(self):
        bookTitle = self.__entryTwo.get()
        if bookTitle:
            book = self.__libraryModel.getBook(bookTitle)
            transStr = self.__libraryModel.getTransactionStatus()
            self.__returnBookTransStatus.set(transStr)
            if book:
                book.returnMe()
                transStr = book.getTransactionStatus()
                self.__returnBookTransStatus.set(transStr)
        #print(bookTitle)

    #Search if book is in Library
    #Bound with <return>
    def __searchBook(self,event):
        bookTitle = self.__entryFive.get()
        if(bookTitle):
            book = self.__libraryModel.getBook(bookTitle)
            #print(bookTitle)
            transStatus = self.__libraryModel.getTransactionStatus()
            #print(transStatus)
            self.__bookSearchStatus.set(transStatus)

    #Search if patron is in library
    #Bound with <return>
    def __searchPatron(self,event):
        patronName = self.__entrySix.get()
        if patronName:
            patron = self.__libraryModel.getPatron(patronName)
            #print(patronName)
            transStatus = self.__libraryModel.getTransactionStatus()
            self.__patronSearchStatus.set(transStatus)

    #Join patron in the Library
    #Bound with <return>
    def __joinLibrary(self,event):
        patronName = self.__entrySeven.get()
        #print(patronName)
        if not self.__libraryModel.isMember(patronName):
            newPatron = Patron(patronName)
            #print(newPatron)
            self.__libraryModel.addPatron(newPatron)
            #print(self.__libraryModel)
            transStatus = self.__libraryModel.getTransactionStatus()
            #print(transStatus)
            self.__patronJoinStatus.set(transStatus)
        else:
            self.__patronJoinStatus("Already a member")
        #print("test")

    #Leave patron from the Library
    #Bound with <Return>
    def __leaveLibrary(self,event):
        patronName = self.__entryEight.get()
        if patronName:
            self.__libraryModel.removePatron(patronName)
            transStatus = self.__libraryModel.getTransactionStatus()
            #print(transStatus)
            self.__patronLeaveStatus.set(transStatus)
        #print(patronName)
        #print("test")

    #Book added to the Library
    def __addBook(self):
        bookTitle = self.__entryNine.get()
        authorName = self.__entryTen.get()
        if bookTitle and authorName:
            newBook = Book(bookTitle,authorName)
            #print(newBook)
            self.__libraryModel.addBook(newBook)
            transStatus = self.__libraryModel.getTransactionStatus()
            #print(transStatus)
            self.__addBookStatus.set(transStatus)
        #print(bookTitle, authorName)

    #Book removed from library
    def __removeBook(self):
        bookTitle = self.__entryEleven.get()
        #self.__entryTwelveLabel.select_clear()
        if bookTitle:
            self.__libraryModel.removeBook(bookTitle)
            transStatus = self.__libraryModel.getTransactionStatus()
            #print(transStatus)
            self.__removeBookStatus.set(transStatus)
        #print(bookTitle)
