

from tkinter import *

class calculator:

    #getInput()
    def getInput(self):
        """
        Takes all values from Entry and stores them into userInput.
        """
        self.userInput = self.entry.get()


    #clearInput()
    def clearInput(self):
        """
        Clears the Entry.
        """
        self.entry.delete(0, END)


    #buttonPress()
    def buttonPress(self, argv):
        """
        Inserts the argument of the button into Entry.
        """
        self.entry.insert(END, argv)


    #evaluate()
    def evaluate(self):
        """
        Uses eval() to evaluate the input.
        Two exceptions:
            1. ZeroDivisionError:   displays "Not a number" to user
            2. SyntaxError:         displays "Input error"
        If eval() is successful, then displays result in Entry.
        """
        self.getInput()
        try:
            self.result = eval(self.userInput)
        except ZeroDivisionError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Not a number")
        except SyntaxError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Input error")
        else:
            self.entry.delete(0, END)
            self.entry.insert(0, self.result)


    #constructor()
    def __init__(self, gui):

        #gui
        gui.title("")
        gui.geometry()

        #Entry
        self.entry = Entry(gui, fg = "black")
        self.entry.grid(row = 0, column = 0, columnspan = 4)

        #Buttons
        bAC = Button(gui, text = "AC", width = 17, height = 3, fg = "red",
        command = lambda: self.clearInput())
        bAC.grid(row = 1, column = 0, columnspan = 3)

        bDiv = Button(gui, text = "/", width = 5, height = 3, fg = "blue",
        command = lambda: self.buttonPress("/"))
        bDiv.grid(row = 1, column = 3)

        b1 = Button(gui, text = "1", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("1"))
        b1.grid(row = 2, column = 0)

        b2 = Button(gui, text = "2", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("2"))
        b2.grid(row = 2, column = 1)

        b3 = Button(gui, text = "3", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("3"))
        b3.grid(row = 2, column = 2)

        bMult = Button(gui, text = "*", width = 5, height = 3, fg = "blue",
        command = lambda: self.buttonPress("*"))
        bMult.grid(row = 2, column = 3)

        b4 = Button(gui, text = "4", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("4"))
        b4.grid(row = 3, column = 0)

        b5 = Button(gui, text = "5", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("5"))
        b5.grid(row = 3, column = 1)

        b6 = Button(gui, text = "6", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("6"))
        b6.grid(row = 3, column = 2)

        bSub = Button(gui, text = "-", width = 5, height = 3, fg = "blue",
        command = lambda: self.buttonPress("-"))
        bSub.grid(row = 3, column = 3)

        b7 = Button(gui, text = "7", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("7"))
        b7.grid(row = 4, column = 0)

        b8 = Button(gui, text = "8", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("8"))
        b8.grid(row = 4, column = 1)

        b9 = Button(gui, text = "9", width = 5, height = 3, fg = "black",
        command = lambda: self.buttonPress("9"))
        b9.grid(row = 4, column = 2)

       
        bAdd = Button(gui, text = "+", width = 5, height = 3, fg = "blue",
        command = lambda: self.buttonPress("+"))
        bAdd.grid(row = 4, column = 3)

        b0 = Button(gui, text = "0", width = 11, height = 3, fg = "black",
        command = lambda: self.buttonPress("0"))
        b0.grid(row = 5, column = 0, columnspan = 2)

        bDot = Button(gui, text = ".", width = 5, height = 3, fg = "blue",
        command = lambda: self.buttonPress("."))
        bDot.grid(row = 5, column = 2)

        bEquals = Button(gui, text = "=", width = 5, height = 3, fg = "green",
        command = lambda: self.evaluate())
        bEquals.grid(row = 5, column = 3)

root = Tk()
calculator(root)
root.mainloop()
