#CMP9134M ADVANCED SOFTWARE ENGINEERING - SIGN UP
#NATHAN JONES
#MAR/FEB 2023

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

def SignUp():

    with open("data.txt", "a") as file: #WITH THE DATA FILE OPEN THE FOLLOWING WILL BE APPEDED TO DATA FILE
        file.write(username.get())      #GETTING THE USERS INPUT OF THEIR USERNAME AND APPEDEDING IT TO THE DATA FILE 
        file.write(" ")                 #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
        file.write(password.get())      #GETTING THE USERS INPUT OF THEIR PASSWORD AND APPEDEDING IT TO THE DATA FILE  
        file.write(" ")                 #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
        file.write(fname.get())         #GETTING THE USERS INPUT OF THEIR FIRST NAME AND APPEDEDING IT TO THE DATA FILE  
        file.write(" ")                 #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
        file.write(sname.get())         #GETTING THE USERS INPUT OF THEIR LAST NAME AND APPEDEDING IT TO THE DATA FILE  
        file.write(" ")                 #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
        file.write(accnum.get())        #GETTING THE USERS INPUT OF THEIR ACCOUNT NUMBER AND APPEDEDING IT TO THE DATA FILE
        file.write(" ")                 #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
        file.write(accname.get())       #GETTING THE USERS INPUT OF THEIR ACCOUNT NAME AND APPEDEDING IT TO THE DATA FILE
        file.write(" ")                 #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
        file.write(dob.get())           #GETTING THE USERS INPUT OF THEIR DOB AND APPEDEDING IT TO THE DATA FILE  
        file.write("\n")                #WRITING AN EMPTY LINE AFTER THE USERS INPUTS FOR THE NEXT USERS ENTRIES
        file.close()                    #CLOSING THE FILE AFTER ALL OF THE DATA HAS BEEN APPENED TO THE DATA FILE
        
        messagebox.showinfo("information", "Your account has been CREATED!") #DISPLAYING A MESSAGE STATING THAT THEIR ACCOUNT HAS BEEN CREATED
        os.startfile("CMPLOGIN.py")                                          #ONCE 'OK' HAS BEEN CLICKED THE LOGIN APPLICATION WILL BE STARTED
        window.destroy()                                                     #CLOSING THE SIGN UP WINDOW AS THE LOGIN WINDOW OPENS


window = Tk() #DEFINING WHAT THE TKINTER WINDOW WILL BE DEFINED AS

window.resizable(0,0)                         #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable(width=FALSE, height=FALSE)   #THE USER CANNOT CHANGE THE SIZE OF THE LOGIN WINDOW
window.title ("CMP BANKING SYSTEM SIGN UP")   #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("500x700")                    #CONFIGURING THE FIXED SIZE OF THE LOGIN WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')          #CONFIGURING THE BACKGROUND OF THE LOGIN WINDOW TO BE WHITE

logo = PhotoImage(file="CMPBANKINGLOGO.png")  #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE LOGIN WINDOW

Logo = Label (window, image=logo)             #CREATING THE LABEL THAT WILL DISPLAY THE CMP BANKING LOGO AT THE TOP OF THE LOGIN WINDOW

S1 = Label(window, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
Title = Label (window, text="CMP BANKING SYSTEM SIGN UP", font='Helvetica 16 bold', background="white") #CREATING A TITLE FOR THE LOGIN WINDOW
S2 = Label(window, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

FName = Label (window, text="Enter First Name:", font='Helvetica 10', background="white")               #CREATING THE LABEL THAT WILL SAY FIRST NAME ABOVE THE ENTRY BOX
fname = Entry (window, background="light grey")                                                         #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR FIRST NAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
SName = Label (window, text="Enter Last Name:", font='Helvetica 10', background="white")                #CREATING THE LABEL THAT WILL SAY LAST NAME ABOVE THE ENTRY BOX
sname = Entry (window, background="light grey")                                                         #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR LAST NAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
DOB = Label (window, text="Enter Date of Birth:", font='Helvetica 10', background="white")              #CREATING THE LABEL THAT WILL SAY DOB ABOVE THE ENTRY BOX
dob = Entry (window, background="light grey")                                                           #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR DOB, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
Username = Label (window, text="Create Username:", font='Helvetica 10', background="white")             #CREATING THE LABEL THAT WILL SAY 'Username' ABOVE THE ENTRY BOX
username = Entry (window, background="light grey")                                                      #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR USERNAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
Password = Label (window, text="Create Password:", font='Helvetica 10', background="white")             #CREATING THE LABEL TAHT WILL SAY 'Password' ABOVE THE ENTRY BOX
password = Entry (window, background="light grey", show="*")                                            #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR PASSOWRD, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
ACCNUM = Label (window, text="Enter Account Number:", font='Helvetica 10', background="white")              #CREATING THE LABEL THAT WILL SAY DOB ABOVE THE ENTRY BOX
accnum = Entry (window, background="light grey")                                                           #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR DOB, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
ACCNAME = Label (window, text="Enter Account Name:", font='Helvetica 10', background="white")              #CREATING THE LABEL THAT WILL SAY DOB ABOVE THE ENTRY BOX
accname = Entry (window, background="light grey")                                                           #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR DOB, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX

S3 = Label(window, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

SignUp = Button (text="     SIGN UP     ", fg="red", command=SignUp) #CREATING THE SIGN UP BUTTON THAT WILL BE DISPLAYED

dob.insert(END,'DD/MM/YYYY')                                         #TELLING THE USER THE FORMAT OF THE ENTRY
username.insert(END,'Your Email Address')                            #TELLING THE USER WHAT TO ENTER FOR THE USERNAME

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
username.pack()     #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR USERNAME
Password.pack()     #DISPLAYING THE PASSWORD LABEL THAT WILL SIT ABOVE THE ENTRY BOX
password.pack()     #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR PASSWORD
ACCNUM.pack()       #DISPLAYING THE ACCOUNT NUMBER LABEL THAT WILL SIT ABOVE THE ENTRY BOX
accnum.pack()       #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR ACCOUNT NUMBER
ACCNAME.pack()      #DISPLAYING THE ACCOUNT NAME LABEL THAT WILL SIT ABOVE THE ENTRY BOX
accname.pack()      #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR ACCOUNT NAME
S3.pack()           #DISPLAYING THE SPACE LABEL
SignUp.pack()       #DISPLAYING THE SIGN UP BUTTON





#CMP9134M ADVANCED SOFTWARE ENGINEERING - SIGN UP
#NATHAN JONES
#MAR/FEB 2023

