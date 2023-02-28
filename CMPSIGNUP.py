#CMP9134M ADVANCED SOFTWARE ENGINEERING - SIGN UP
#NATHAN JONES
#FEB 2023

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 

import datetime
import sys
import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import socket      #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 

def donothing():            #CREATING THE FUNCTION THAT WILL LITERALLY DO NOTHING BY THE USE OF THE 'pass' FUNCTION WITHIN PYTHON
    pass                    #CALLING THE 'pass' FUNCTION TO DO NOTHING

def Login():
    os.startfile("CMPLOGIN.py")
    window.destroy()

def SignUp():

    with open("data.txt", "a") as file:
        file.write(username.get())
        file.write(" ")
        file.write(password.get())
        file.write(" ")
        file.write(fname.get())
        file.write(" ")
        file.write(sname.get())
        file.write(" ")
        file.write(dob.get())
        file.write("\n")
        file.close()
        messagebox.showinfo("information", "Your account has been CREATED!")


window = Tk() #DEFINING WHAT THE TKINTER WINDOW WILL BE DEFINED AS

window.resizable(0,0)                         #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable(width=FALSE, height=FALSE)   #THE USER CANNOT CHANGE THE SIZE OF THE LOGIN WINDOW
window.title ("CMP BANKING SYSTEM SIGN UP")   #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("500x600")                    #CONFIGURING THE FIXED SIZE OF THE LOGIN WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')          #CONFIGURING THE BACKGROUND OF THE LOGIN WINDOW TO BE WHITE

logo = PhotoImage(file="CMPBANKINGLOGO.png")  #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE LOGIN WINDOW

Logo = Label (window, image=logo)             #CREATING THE LABEL THAT WILL DISPLAY THE CMP BANKING LOGO AT THE TOP OF THE LOGIN WINDOW

S1 = Label(window, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
Title = Label (window, text="CMP BANKING SYSTEM SIGN UP", font='Helvetica 16 bold', background="white") #CREATING A TITLE FOR THE LOGIN WINDOW
S2 = Label(window, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

FName = Label (window, text="Enter First Name:", font='Helvetica 11', background="white")               #CREATING THE LABEL THAT WILL SAY FIRST NAME ABOVE THE ENTRY BOX
fname = Entry (window, background="light grey")                                                         #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR FIRST NAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
SName = Label (window, text="Enter Last Name:", font='Helvetica 11', background="white")                #CREATING THE LABEL THAT WILL SAY LAST NAME ABOVE THE ENTRY BOX
sname = Entry (window, background="light grey")                                                         #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR LAST NAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
DOB = Label (window, text="Enter Date of Birth:", font='Helvetica 11', background="white")              #CREATING THE LABEL THAT WILL SAY DOB ABOVE THE ENTRY BOX
dob = Entry (window, background="light grey")                                                           #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR DOB, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
Username = Label (window, text="Create Username:", font='Helvetica 11', background="white")             #CREATING THE LABEL THAT WILL SAY 'Username' ABOVE THE ENTRY BOX
UsernameDesc = Label (window, text="Use Your Email Address", font='Helvetica 9', background="white")    #CREATING THE LABEL THAT WILL SAY WHAT TO ENTER IN THE USERNAME BOX
username = Entry (window, background="light grey")                                                      #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR USERNAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
Password = Label (window, text="Create Password:", font='Helvetica 11', background="white")             #CREATING THE LABEL TAHT WILL SAY 'Password' ABOVE THE ENTRY BOX
password = Entry (window, background="light grey", show="*")                                            #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR PASSOWRD, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
S3 = Label(window, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

SignUp = Button (text="     SIGN UP     ", fg="red", command=SignUp)                                    #CREATING THE SIGN UP BUTTON THAT WILL BE DISPLAYED

Logo.pack()         #DISPLAYING THE LOGO LABEL
S1.pack()           #DISPLAYING THE SPACE LABEL
Title.pack()        #DISPLAYING THE TITLE OF THE WINDOW
S2.pack()           #DISPLAYING THE SPACE LABEL
FName.pack()        #DISPLAYING THE FIRST NAME LABEL THAT WILL SIT ABOVE THE ENTRY BOX
fname.pack()        #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR FIRST NAME
SName.pack()        #DISPLAYING THE LAST NAME LABEL THAT WILL SIT ABOVE THE ENTRY BOX
sname.pack()        #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR LAST NAME
DOB.pack()          #DISPLAYING THE DOB LABEL THAT WILL SIT ABOVE THE ENTRY BOX
dob.pack()          #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR DOB
Username.pack()     #DISPLAYING THE USERNAME LABEL THAT WILL SIT ABOVE THE ENTRY BOX
UsernameDesc.pack() #DISPLAYING THE USERNAME DESCRIPTION LABEL THAT WILL SIT ABOVE THE ENTRY BOX
username.pack()     #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR USERNAME
Password.pack()     #DISPLAYING THE PASSWORD LABEL THAT WILL SIT ABOVE THE ENTRY BOX
password.pack()     #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR PASSWORD
S3.pack()           #DISPLAYING THE SPACE LABEL
SignUp.pack()       #DISPLAYING THE SIGN UP BUTTON



#CMP9134M ADVANCED SOFTWARE ENGINEERING - SIGN UP
#NATHAN JONES
#FEB 2023

