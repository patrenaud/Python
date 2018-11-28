# Click Counter
# Demonstrates binding an event with an event handler

from tkinter import *

class Application(Frame):
    """ GUI application wich counts button clicks """
    def __init__(self, master):
        """ Initialize the frame """
        super(Application, self).__init__(master)
        self.grid()
        self.btn_clicks = 0
        self.createWidget()

    def createWidget(self):
        self.btn = Button(self)
        self.btn.configure(text = "Total clicks: 0")
        self.btn.configure(command = self.updateCount)
        self.btn.grid()

    def updateCount(self):
        """ Increase click count and display """
        self.btn_clicks += 1
        self.btn.configure(text = "Total clicks: " + str(self.btn_clicks))

# Main
root = Tk()
root.title("Click Counter")
root.geometry("400x500")
app = Application(root)

root.mainloop()
