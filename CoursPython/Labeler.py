# Labeler
# Demonstrate a label

from tkinter import *

# create the root window
root = Tk()
root.title("Labeler")

root.geometry("400x500")

# create a frame in the window to hold other widget
app = Frame(root)
app.grid()

# create a label in the frame
lbl = Label(app, text = "I'm a label!")
lbl.grid()

# start the window's event loop
root.mainloop()
