# Lazy Buttons
# Demonstrate creating buttons

from tkinter import *

# create new window
root = Tk()
root.title("Lazy Buttons")
root.geometry("400x500")

# create frame in the window to hold other widgets
app = Frame(root)
app.grid()

# create a button in the frame in the window
btn1 = Button(app, text = "I do Nothing!")
btn1.grid()

# create another button
btn2 = Button(app)
btn2.grid()
btn2.configure(text = "Me too!")

# create a 3rd button
btn3 = Button(app,)
btn3.grid()
btn3["text"] = "Same here! ^^"

# kickoff the root window
root.mainloop()
