# Lazy Button 2
# Demonstrate using a class Tkinter
from tkinter import *

class Application(Frame):
    """ A GUI app with 3 Buttons"""
    def __init__(self, master):
        """ Initialize the Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """ Create three buttons that do nothing """
        # create first button        
        self.btn1 = Button(self, text = "I still do nothing")
        self.btn1.grid()

        self.btn2 = Button(self)
        self.btn2.grid()
        self.btn2.configure(text = "Me too!")
        
        self.btn3 = Button(self)
        self.btn3.grid()
        self.btn3["text"] = "Same here !"

# Main
root = Tk()
root.title("Lazy button 2: the reckoning")
root.geometry("400x500")
app = Application(root)
root.mainloop()
