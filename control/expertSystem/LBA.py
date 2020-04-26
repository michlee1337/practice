# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:01:19 2020

@author: Austin Perzben
"""

# The code here will ask the user for input based on the askables
# It will check if the answer is known first

import os
from tkinter import Tk, StringVar
from tkinter.ttk import Button, Label, Frame
from itertools import count
# Check if pyswip package needs to be installed

from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog() # Global handle to interpreter

retractall = Functor("retractall")
known = Functor("known",3)

marker = 0
responses = []

# Define foreign functions to read user input and write to the screen
def write_py(X):
    
    sys.stdout.flush()
    return True

def read_py(A,V,Y):
    global marker
    if isinstance(Y, Variable):
        question.config(text=str(A) + " is " + str(V) + "? ")
        output.config(text=)
        y_button.wait_variable(var)
        responses.append(var)
        response = str(responses[marker])
        print(type(response))
        marker += 1
        Y.unify(response)
        return True
    else:
        return False

registerForeign(read_py, arity = 3)
registerForeign(write_py, arity = 1)

prolog.consult("ES.pl") # open the KB for consulting
call(retractall(known))

# GUI
root = Tk()
root.title('COVID-19 Risk Assessment')
root.iconbitmap(default='covid.ico')
root.geometry('480x720')
var = StringVar()
frame = Frame(root)
frame.pack(anchor='center',padx=20, pady=20)
question = Label(frame,text='')
question.grid(column=0,row=1,columnspan=2)
y_button = Button(frame, text='Yes', command=lambda: var.set("yes"))
y_button.grid(column=0,row=5)
n_button = Button(frame, text='No', command=lambda: var.set("no"))
n_button.grid(column=1,row=5)
output = Label(frame,text='')
output.grid(column=0,row=3,columnspan=2)

action = [s for s in prolog.query("action(X).", maxresult=1)]
print("You should " + (action[0]['X'] + "." if action else "hang tight."))

output.config(text=result)
root.mainloop()


