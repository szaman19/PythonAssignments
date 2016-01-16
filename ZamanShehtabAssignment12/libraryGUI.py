import tkinter as Tk
import tkinter.messagebox

class LibraryGUI:

    def __init__(self):
        self.__win = Tk.Tk()
        self.__win.title('Library')

        self.__top = Tk.Frame(self.__win)
        self.__topOne = Tk.Frame(self.__win)
        self.__topTwo = Tk.Frame(self.__win)
        self.__topThree = Tk.Frame(self.__win)
        self.__topFour = Tk.Frame(self.__win)
            #
        self.__mid = Tk.Frame(self.__win)
        self.__midOne = Tk.Frame(self.__win)
        self.__midTwo = Tk.Frame(self.__win)
        self.__midThree = Tk.Frame(self.__win)
        self.__midFour = Tk.Frame(self.__win)
            #
        self.__bottom = Tk.Frame(self.__win)

            #Checkout Books Label
        self.__cbLabel = Tk.Label\
        (self.__top,text="Checkout Books")
            #Return Books Label
        self.__rbLabel = Tk.Label\
        (self.__top,text="Return Books")
            #Book Label
        self.__bLabel = Tk.Label\
        (self.__mid,text="Book")
            #Patron Label
        self.__pLabel = Tk.Label\
        (self.__mid, text="Patron")
            #Join Label
        self.__jLabel = Tk.Label\
        (self.__bottom,text="Join")
            #Leave Label
        self.__lLabel = Tk.Label\
        (self.__bottom, text="Leave")
            #
        self.__entryOneLabel = Tk.Label\
        (self.__topOne, text="Title")
        self.__entryOne = Tk.Entry\
        (self.__topOne,width=30)
            #
        self.__entryTwoLabel = Tk.Label\
        (self.__topOne, text="Title")
        self.__entryTwo = Tk.Entry\
        (self.__topOne,width=30)
            #
        self.__entryThreeLabel = Tk.Label\
        (self.__topTwo, text="Patron")
        self.__entryThree = Tk.Entry\
        (self.__topTwo,width=30)
            #
        self.__entryFourLabel = Tk.Label\
        (self.__topTwo, text="Patron")
            #
        self.__cbButton = Tk.Button\
        (self.__topThree,text="Checkout Book")

        self.__rbButton = Tk.Button\
        (self.__topThree,text="Return Book")

        self.__bookLabel = Tk.Label\
        (self.__midOne,text="Title")
        self.__entryFive = Tk.Entry\
        (self.__midOne,width=30)

        self.__patronLabel = Tk.Label\
        (self.__midOne,text="Name")
        self.__entrySix = Tk.Entry\
        (self.__midOne,width=30)



        self.__cbLabel.pack(side="left")
        self.__rbLabel.pack(side="left")

        self.__entryOneLabel.pack(side="left")
        self.__entryOne.pack(side="left")

        self.__entryTwoLabel.pack(side="left")
        self.__entryTwo.pack(side="left")

        self.__entryThreeLabel.pack(side="left")
        self.__entryThree.pack(side="left")
        self.__cbButton.pack(side="right")
        self.__rbButton.pack(side="right")

        self.__entryFourLabel.pack(side="left")

        self.__bLabel.pack(side="left")
        self.__pLabel.pack(side="right")

        self.__bookLabel.pack(side="left")
        self.__entryFive.pack(side="left")
        self.__patronLabel.pack(side="left")
        self.__entrySix.pack(side="left")

        self.__jLabel.pack(side="left")
        self.__lLabel.pack(side="right")

        self.__top.pack()
        self.__topOne.pack()
        self.__topTwo.pack()
        self.__topThree.pack()
        self.__topFour.pack()
        self.__mid.pack()
        self.__midOne.pack()
        self.__bottom.pack()

        Tk.mainloop()
