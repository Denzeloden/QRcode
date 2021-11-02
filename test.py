from tkinter import *
from tkinter import filedialog

# root widget
root = Tk()

# Open file dialog box
root.filename = filedialog.askopenfilename(initialdir="/", title="Select A Folder")
# Create an Entry widget for user input
e = Entry(root, width=50, borderwidth=5)
# Enter default text in entry
e.insert(0, "Enter Name")
# Button click event function
def myClick():
    myLabel = Label(root, text="You did it!!")
    myLabel.grid(row=4, column=0)
def myEntry():
    myLabel3 = Label(root, text=e.get())
    myLabel3.grid(row=4, column=3)

# Create a dropdown menu widget
# Create tkinter variable
clicked = IntVar()
# Create a list for dropdown menu
options = [
    0,
    1,
    2,
    3,
    4
]
myCanvas = Canvas(root, bg="white", height=300, width=300)
myCanvas.grid(row=5, column=3)

display = PhotoImage(file="Good.png")
myCanvas.create_image(0, 0, anchor=NW, image=display)
# set default
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options).grid(row=6, column=0)


# Create a label widget
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Denzel!")

# Create a Button widget
myButton = Button(root, text="Click Me!")

# Create a Button widget and change its size with padx/pady
myButton2 = Button(root, text="Click Me!", padx=25, pady=5)

# Create a Button widget that has a click event
myButton = Button(root, text="Click Me!", command=myClick)

# Create a Button widget with color
myButton3 = Button(root, text="Click Me!", command=myClick, fg="green", bg="yellow")

# Create a button to accept and entry
myButton4 = Button(root, text="Enter Name", command=myEntry, fg="black", bg="gray").grid(row=5, column=2)
# Pack it into root frame
# myLabel.pack()

# Position label with grid
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Position Button with grid
myButton.grid(row=2, column=0)
myButton2.grid(row=3, column=0)
myButton3.grid(row=4, column=0)

# Position Entry with grid
e.grid(row=5, column=0)
# Create program loop
root.mainloop()
