# QRCode generator
import glob
import os
import tkinter
import qrcode
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog, colorchooser, messagebox, ttk
import time
import copy

# tkinter root widget
from PIL import ImageTk

root = Tk()
icon = PhotoImage(file='Oden Logo.png')
root.iconphoto(False, icon)
# Create and save qrcode

qrsave = Entry(root, width=75, borderwidth=5)
qrsave.grid(row=6, column=3)
# Entry for batch number
qty = Entry(root, width=2, borderwidth=5)
qty.grid(row=8, column=2)


def create():
    # combines file location and file name
    completename = os.path.join(qrfilelocation.get(), qrsave.get())
    # Qr code style
    qr = qrcode.QRCode(
        version=qrversion.get(),
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=qrboxsize.get(),
        border=qrborder.get(),
    )
    qr.add_data(qrdata.get())
    qr.make(fit=True)
    img = qr.make_image(fill_color=color_code, back_color=color_codebg)
    img.save(completename)
    display = PhotoImage(file=completename)
    # Hold image in memory. Tkinters garbage collection will get rid of the image from the main loop otherwise
    myCanvas.image = display
    myCanvas.create_image(0, 0, image=display, anchor="nw")


# Creates a batch of QR codes
def batch():
    # disables save as
    qrsave.config(state='disabled')
    if qty.get() == "":
        messagebox.showerror("Error", "Input a batch quantity")

    for i in range(int(qty.get())):
        datanum = copy.copy(int(qrdata.get()))
        datanum += 1
        datanum = str(datanum)
        qrdata.delete(0, 'end')
        qrdata.insert(0, datanum)

        # combines file location, data input and .svj to save the qrcode with its data input as its file name
        completename = os.path.join(qrfilelocation.get(), str(datanum) + ".svj")
        # Qr code style
        qr = qrcode.QRCode(
            version=qrversion.get(),
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=qrboxsize.get(),
            border=qrborder.get(),
        )
        qr.add_data(str(datanum))
        qr.make(fit=True)
        img = qr.make_image(fill_color=color_code, back_color=color_codebg)
        img.save(completename)
        display = PhotoImage(file=completename)
        # Hold image in memory. Tkinters garbage collection will get rid of the image from the main loop otherwise
        myCanvas.image = display
        myCanvas.create_image(0, 0, image=display, anchor="nw")
        start(i)
        print(i)


def start(i):
    #starts load bar
    root.update_idletasks()
    percentnum = ((i+1)/int(qty.get()))*100 # Calculates percentage
    percent.set(str(((i+1)/int(qty.get()))*100) + "%") # sets label to percentage
    load['value'] = percentnum
    time.sleep(1)
    if percentnum == 100.0:
        percent.set('COMPLETE')



def fileLocation():
    folderpath = filedialog.askdirectory(
        title="Choose File",
        initialdir='/'
    )
    qrfilelocation.insert(0, folderpath)


def choose_color():
    # variable to store hexadecimal code of color
    global color_code
    color_code = colorchooser.askcolor(title="Choose color")[1]
    myLabel8 = Label(bf, text=" ", bg=color_code).grid(row=1, column=1)


def choose_colorbg():
    # variable to store hexadecimal code of color
    global color_codebg
    color_codebg = colorchooser.askcolor(title="Choose color")[1]
    myLabel9 = Label(bf, text=" ", bg=color_codebg).grid(row=2, column=1)


# Create a list for dropdown menu
options = [
    1,
    2,
    3,
    4
]
optionsbs = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    10
]
optionsbor = [
    4, 5, 6,
    7, 8, 9,
    10
]
# Labels
myLabel = Label(root, text="Version", bg="light gray").grid(row=1, column=0)
myLabel2 = Label(root, text="Box Size", bg="light gray").grid(row=3, column=0)
myLabel3 = Label(root, text="Border size", bg="light gray").grid(row=5, column=0)
myLabel4 = Label(root, text="             ", bg="light gray").grid(row=1, column=2)
myLabel5 = Label(root, text="Input Data", bg="light gray").grid(row=1, column=3)
myLabel6 = Label(root, text="File Location", bg="light gray").grid(row=3, column=3)
myLabel7 = Label(root, text="Save As", bg="light gray").grid(row=5, column=3)
#myLabel8 = Label(root, text="QTY", bg="light gray").grid(row=7, column=2)
# Create tkinter variable
qrversion = IntVar()
qrboxsize = IntVar()
qrborder = IntVar()

# set default and create dropdown menus
qrversion.set(options[0])
drop = OptionMenu(root, qrversion, *options).grid(row=2, column=0)
qrboxsize.set(optionsbs[9])
drop2 = OptionMenu(root, qrboxsize, *optionsbs).grid(row=4, column=0)
qrborder.set(optionsbor[0])
drop3 = OptionMenu(root, qrborder, *optionsbor).grid(row=6, column=0)
# Create entry field for data
qrdata = Entry(root, width=75, borderwidth=5)
qrdata.grid(row=2, column=3)
# Save file location
qrfilelocation = Entry(root, width=75, borderwidth=5)
qrfilelocation.grid(row=4, column=3)
# Update display
list_of_files = glob.glob(
    'C:/Users/Denzel Oden/PycharmProjects/KGM-QRcode_Generator/*.png')  # * means all if need specific format then *.csv
myCanvas = Canvas(root, bg="Black", height=300, width=300)
myCanvas.grid(row=7, column=3)
allcommands = lambda: [create()]
myButton = Button(root, text="Create", command=allcommands, fg="black", bg="gray", padx=25, pady=5,
                  anchor=tkinter.SW).grid(row=9, column=0)
fileButton = Button(root, text="...", command=fileLocation, fg="black", bg="gray").grid(row=4, column=4)
# Frame to hold buttons
bf = tkinter.Frame(root, bg="light gray")
bf.grid(row=7, column=0, sticky="nw")
myLabel8 = Label(bf, text="", bg="light gray").grid(row=0, column=0)
fgButton = Button(bf, text="QR Color", command=choose_color, fg="black", bg="gray").grid(row=1, column=0, sticky="nw")
bgButton = Button(bf, text="BG Color", command=choose_colorbg, fg="black", bg="gray").grid(row=2, column=0)
batchButton = Button(root, text="Create Batch", command=batch, fg="black", bg="gray", anchor=tkinter.SW, padx=9, pady=5).grid(row=8,
                                                                                                              column=0)
# Background color
root.configure(bg='light gray')
# Loading bar
# Determinate full bar
load = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
load.grid(row=8, column=3)
percent = StringVar()
percent_label = Label(root, textvariable=percent, bg="Light Gray").grid(row=9, column=3)

root.mainloop()
