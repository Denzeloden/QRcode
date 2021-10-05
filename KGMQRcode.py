# QRCode generator
import glob
import os
import tkinter
from os.path import exists

import qrcode
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog, colorchooser, messagebox
import time
import copy
import re

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
    try:
        # combines file location and file name
        completename = os.path.join(qrfilelocation.get(), qrsave.get())
        file_exists = exists(completename)
        if file_exists == True:# Checks to see if QR esist
            messagebox.showerror("Error", "This Code already Exist!!!")
        else:
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
    except OSError as err:
        messagebox.showerror("OS error: {0}".format(err))
    except ValueError:
        messagebox.showerror("Could not convert data to an integer.")
    except:
        messagebox.showerror("Unexpected error:", sys.exc_info()[0])
        raise

# Creates a batch of QR codes
def batch():
    # disables save as
    qrsave.config(state='disabled')
    if qty.get() == "":
        messagebox.showerror("Error", "Input a batch quantity")
    # initializes datanum with a copy of the current qrdata
    try:

        datanum = copy.copy(int(qrdata.get()))
        for i in range(int(qty.get())):
            #datanum = copy.copy(int(qrdata.get()))
            #datanum += 1
            datanum = prefix.get() + str(datanum)
            qrdata.delete(0, 'end')
            qrdata.insert(0,  datanum)

            # combines file location, data input and .svj to save the qrcode with its data input as its file name
            completename = os.path.join(qrfilelocation.get(), str(datanum) + ".svj")
            file_exists = exists(completename)
            if file_exists == True:  # Checks to see if QR esist
                messagebox.showerror("Error", "This Serial already Exist!!!: {0}".format(datanum))
                qrdata.delete(0, 'end')
                break # ends loop
            else:
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
                # datacopy holds a copy of the qrdata with the prefix
                datacopy = copy.copy(str(qrdata.get()))
                # the qrdata field is then cleared
                qrdata.delete(0, 'end')
                dataslice = datacopy[datacopy.find("-"):] # finds the "-" in data copy and slices from that point to the end of the string
                # data copy is then formatted to only contain the number of the serial for iteration
                datacopy = re.sub('[^0-9 \n\.]', '', dataslice)
                # the formatted data is then inserted into qrdata to continue iteration
                qrdata.insert(0, datacopy)
                datacopyint = int(datacopy)# assigns the int value of data copy to the datacopyint variable
                datacopyint += 1 # increments datacopy
                datanum = datacopyint# assignes datacopy int to datanum
        return datanum
    except NameError as err:
        messagebox.showerror("Error", "Name Error: {0}".format(err))
        qrdata.delete(0, 'end')





def start(i):
    #starts load bar
    percent.set("")
    root.update_idletasks()
    percentnum = int(((i+1)/int(qty.get()))*100) # Calculates percentage
    percent.set(str(int(((i+1)/int(qty.get()))*100)) + "%") # sets label to percentage
    load['value'] = percentnum
    time.sleep(0.10)
    if percentnum == 100:
        percent.set('COMPLETE')
        qrsave.config(state='normal')


def fileLocation():
    folderpath = filedialog.askdirectory(
        title="Choose File",
        initialdir='/'
    )
    qrfilelocation.insert(0, folderpath)


def choose_color():
    # variable to store hexadecimal code of color
    global color_code
    color_code = colorchooser.askcolor(title="Choose color", initialcolor='Black')[1]
    myLabel8 = Label(bf, text="  ", bg=color_code, anchor='w').grid(row=3, column=1)


def choose_colorbg():
    # variable to store hexadecimal code of color
    global color_codebg
    color_codebg = colorchooser.askcolor(title="Choose color", initialcolor='White')[1]
    myLabel9 = Label(bf, text="  ", bg=color_codebg).grid(row=4, column=1)


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
#myLabel10 = Label(root, text="QTY", bg="light gray").grid(row=7, column=2)
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
myCanvas = Canvas(root, bg="Black", height=275, width=275)
myCanvas.grid(row=7, column=3)
allcommands = lambda: [create()]
myButton = Button(root, text="Create", command=allcommands, fg="black", bg="gray", width=12, pady=5,
                  anchor=CENTER).grid(row=9, column=0)
fileButton = Button(root, text="...", command=fileLocation, fg="black", bg="gray").grid(row=4, column=4)
# Frame to hold buttons
bf = tkinter.Frame(root, bg="light gray")
bf.grid(row=7, column=0, sticky="nw")
myLabel8 = Label(bf, text="", bg="light gray").grid(row=0, column=0)
fgButton = Button(bf, text="QR Color", command=choose_color, fg="black", bg="gray", width=8).grid(row=3, column=0, sticky="nw")
bgButton = Button(bf, text="BG Color", command=choose_colorbg, fg="black", bg="gray", width=8).grid(row=4, column=0, sticky="nw")
batchButton = Button(root, text="Create Batch", command=batch, fg="black", bg="gray", anchor=CENTER, width=12, pady=5).grid(row=8,
                                                                                                              column=0)
# Default color Labels
#myLabel8 = Label(bf, text="  ", bg='Black', anchor='w').grid(row=3, column=1)
#myLabel9 = Label(bf, text="  ", bg='White').grid(row=4, column=1)
# Background color
root.configure(bg='light gray')
# Loading bar
# Determinate full bar
load = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
load.grid(row=8, column=3)
percent = StringVar()
percent_label = Label(root, textvariable=percent, bg="Light Gray").grid(row=9, column=3)
# Prefix entry
prefix_label = Label(bf, text="PREFIX", bg="light gray").grid(row=1, column=0)
prefix = Entry(bf, width=10, borderwidth=5)
prefix.grid(row=2, column=0)
root.mainloop()
