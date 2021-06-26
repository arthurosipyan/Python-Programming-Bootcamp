# ---------- TKINTER TUTORIAL 2 ----------

# Here I'll show how to use the widgets label, entry
# button, check button, radio buttons and combo boxes

# Get the standard library for Tk
from tkinter import *

# Get the newest widget themes from Tk 8.5
from tkinter import ttk


def set_entry(*args):
    entry_1_txt.set("Hello")


def chk_but_changed(*args):
    entry_1_txt.set(chk_but_1_txt.get())


def radio_changed(*args):
    entry_1_txt.set(radio_but_1_val.get())


def combo_changed(*args):
    entry_1_txt.set(combo_1_val.get())


root = Tk()
root.title("Calculator")

frame = ttk.Frame(root, padding="10 10 10 10")

# ---------- GRID GEOMETRY MANAGER  ----------
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ----- LABELS -----
# Used to get and set value of the label
label_1_txt = StringVar()
# Define the parent and text in the label
label_1 = ttk.Label(frame, text='Data :')
label_1.grid(column=1, row=1, sticky=(W, E))

# To change a value you must attach to the StringVar class
label_1['textvariable'] = label_1_txt
label_1_txt.set('Data ')

# ----- ENTRY -----
# Used to get and set the value of the entry
entry_1_txt = StringVar()
# Define the number of characters long and the StringVar
# it is associated with
entry_1 = ttk.Entry(frame, width=7, textvariable=entry_1_txt)
entry_1.grid(column=2, row=1, sticky=(W, E))

# You can get values by using get on a StringVar
entry_1_txt.set(label_1_txt.get())

# ----- BUTTON -----
# Assign text in button and the function to call when clicked
button_1 = ttk.Button(frame, text='Click', command=set_entry)
button_1.grid(column=3, row=1, sticky=(W, E))

# You can disable the button
button_1['state'] = 'disabled'
button_1['state'] = 'enable'

# Check if it is disabled (1 = True, 0 = False)
entry_1_txt.set(button_1.instate(['disabled']))

# ----- CHECK BUTTON -----
chk_but_1_txt = StringVar()
# Text to display next to it, function to call, StringVar,
# value assigned when check and not checked
chk_but_1 = ttk.Checkbutton(frame, text='Feelings',
                            command=chk_but_changed,
                            variable=chk_but_1_txt,
                            onvalue='Happy', offvalue='Sad')
chk_but_1.grid(column=4, row=1, sticky=(W, E))

# ----- RADIO BUTTONS -----
# Only 1 radio button can be selected at a time
# Shared StringVar
radio_but_1_val = StringVar()
# Parent, text assigned, StringVar, value assigned to StringVar,
# function to call on event
red_r_but = ttk.Radiobutton(frame, text='Red',
                            variable=radio_but_1_val,
                            value='Red', command=radio_changed)
blue_r_but = ttk.Radiobutton(frame, text='Blue',
                             variable=radio_but_1_val,
                             value='Blue', command=radio_changed)
green_r_but = ttk.Radiobutton(frame, text='Green',
                              variable=radio_but_1_val,
                              value='Green', command=radio_changed)
red_r_but.grid(column=2, row=2, sticky=(W, E))
blue_r_but.grid(column=3, row=2, sticky=(W, E))
green_r_but.grid(column=4, row=2, sticky=(W, E))

# Label for radio buttons
label_2 = ttk.Label(frame, text='Fav Color')
label_2.grid(column=1, row=2, sticky=(W, E))

# ----- COMBOBOX -----
# Drop down boxes that contain a list of values
combo_1_val = StringVar()
combo_1 = ttk.Combobox(frame, textvariable=combo_1_val)
label_3 = ttk.Label(frame, text='Size')
label_3.grid(column=1, row=3, sticky=(W, E))

# Assign values to the combobox
combo_1['values'] = ('Small', 'Medium', 'Large')
combo_1.grid(column=2, row=3, sticky=(W, E))

# Call a function when combobox is changed
combo_1.bind('<<ComboboxSelected>>', combo_changed)

# A loop that executes until the application exits
root.mainloop()
