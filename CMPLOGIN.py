#CMP9134M ADVANCED SOFTWARE ENGINEERING - LOGIN
#NATHAN JONES
#FEB/MAR 2023

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 

import datetime    #ALLOWS ACCESS TO CURRETN DATE AND TIME OF THE SYTEM
import sys         #ALLOWS ACCESS TO THE SYSTEM FOR VARIOUS TASKS LIKE STARTING FILES
import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import socket      #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import getpass     #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 

TRYS = 0           #KEEPING COUNT OF HOW MANY TRYS THE USER HAS HAD WHEN LOGGING IN
trys = 2           #USED TO CREATE A COUNT DOWN OF HOW MANY MORE ATTEMPTS THE USER HAS FOR THE LOG IN 

def donothing():   #CREATING THE FUNCTION THAT WILL LITERALLY DO NOTHING BY THE USE OF THE 'pass' FUNCTION WITHIN PYTHON
    pass           #CALLING THE 'pass' FUNCTION TO DO NOTHING

def Login():
    global TRYS    #IMPORTING THE 'TRYS' ARRAY TO KEEP TRACK OF HOW MANY ATTEMPTS THEY HAVE HAD AT LOGGING IN
    global trys    #IMPORTING THE 'trys' ARRAY TO CREATE A COUNT DOWN OF HOW MANY MORE ATTEMPTS THEY HAVE AT LOGGING IN
    
    uname = username.get()      #TAKING THE USER'S INPUT OF THEIR USERNAME FROM THE ENTRY BOX
    pword = password.get()      #TAKING THE USER'S INPUT OF THEIR PASSWORD FROM THE ENTRY BOX
    accnum = accountnum.get()   #TAKING THE USER'S INPUT OF THEIR ACCOUNT NUMBER FROM THE ENTRY BOX

    for line in open("data.txt","r").readlines():                       #READING EACH LINE WITHIN THE 'data' FILE
        data = line.split()                                             #SPLITTING EACH WORD ON THE SPACE AND STORING THE RESULTS IN A LIST OF TWO STRINGS
        name = data[2]                                                  #ASSIGING THE 3RD ELEMENT IN THE FILE TO BE 'name'
        ID = data[0]                                                    #ASSIGING THE 1ST ELEMENT IN THE FILE TO BE 'ID'
        acc = data[4]                                                   #ASSIGING THE 5TH ELEMENT IN THE FILE TO BE 'acc'
        accname = data[5]
        if uname == data[0] and pword == data[1] and accnum == data[4]: #IF THE USERNAME AND PASSWORD MATCH THE FOLLOWING TAKES PLACE
            messagebox.showinfo("welcome", "You Are Logged In!")        #DISPLAYS A MESSAGE TO THE USER STATING THEY HAVE LOGGED IN 
            with open("temp.txt", "w") as file:                         #WITH THE TEMP FILE OPEN THE FOLLOWING WILL BE WRITTEN TO TEMP FILE
                file.write(name)                                        #GETTING THE USERS NAME ASSOCIATED WITH THE ACCOUNT AND WRTITING IT TO THE TEMP FILE
                file.write(" ")                                         #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
                file.write(ID)                                          #GETTING THE USERS NAME ASSOCIATED WITH THE ACCOUNT AND WRTITING IT TO THE TEMP FILE
                file.write(" ")                                         #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
                file.write(acc)                                         #GETTING THE USERS ACCOUNT NUMBER ASSOCIATED WITH THE ACCOUNT AND WRTITING IT TO THE TEMP FILE
                file.close()                                            #CLOSING THE FILE AFTER ALL OF THE DATA HAS BEEN WRITTEN TO THE TEMP FILE
            os.system('CMPBS.py')                                       #STARTING THE MAIN BANKING PROGRAM WITH THE USERS CREDENTIALS
            window.destroy()
            
        elif uname != data[0] and pword != data[1] and accnum != data[4]:   #IF THE USERNAME AND/OR PASSWORD DO NOT MATCH ANY OF THE USERNAME/PASSWORD SET THE FOLLOWING STATEMENTS WILL COME INTO PLAY
            if trys == 0:                                                                                        #IF THE USER HAS 0 TRYS LEFT THEN THE FOLLOWING WILL TAKE PLACE
                messagebox.showinfo("   ERROR!   ", """  Your username and/or password was incorrect!                                                        
                         You have """+str(trys)+str(" attempts left! And Have been LOCKED OUT!") , icon="error") #DISPLAYING THE ERROR MESSAGE BOX STATING THEY HAVE BEEN LOCKED OUT
                window.destroy()                                                                                 #CLOSING THE LOGIN APPLICATION AFTER THE 'OK' HAS BEEN CLICKED ON THE MESSAGE BOX
                 
            elif trys > 0:                                                                                       #IF THE USER HAS MORE THAN 0 TRYS LEFT THEN THE FOLLOWING ACTIONS TAKE PLACE
                messagebox.showinfo("   ERROR!   ", """  Your username and/or password was incorrect!                                                        
                         You have """+str(trys)+str(" attempts left!") , icon="error")                           #DISPLAYING THE ERROR MESSAGE BOX WITH ATTEMPTS LEFT
                TRYS = TRYS+1                                                                                    #ADDS +1 TO THE 'TRYS' ARRAY TO KEEP COUNT
                trys = trys-1                                                                                    #TAKES -1 AWAY FROM THE 'trys' ARRAY TO DISPLAY REMAINDER OF ATTMEPTS 
        
def SignUp():
    os.system('CMPSIGNUP.py')    #STARTING THE SIGN UP APPLICATION FOR THE USER TO SIGN UP IF THEY DO NOT HAVE AN ACCOUNT
    window.destroy()             #CLOSING THE LOGIN APPLICATION 

window = Tk() #DEFINING WHAT THE TKINTER WINDOW WILL BE DEFINED AS

window.resizable(0,0)                         #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable(width=FALSE, height=FALSE)   #THE USER CANNOT CHANGE THE SIZE OF THE LOGIN WINDOW
window.title ("CMP BANKING SYSTEM")           #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("500x600")                    #CONFIGURING THE FIXED SIZE OF THE LOGIN WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')          #CONFIGURING THE BACKGROUND OF THE LOGIN WINDOW TO BE WHITE

logo = PhotoImage(file="CMPBANKINGLOGO.png") #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE LOGIN WINDOW

Logo = Label (window, image=logo)            #CREATING THE LABEL THAT WILL DISPLAY THE CMP BANKING LOGO AT THE TOP OF THE LOGIN WINDOW

S1 = Label(window, text=" ", background="white")                                                      #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
Title = Label (window, text="CMP BANKING SYSTEM LOGIN", font='Helvetica 14 bold', background="white") #CREATING A TITLE FOR THE LOGIN WINDOW
S2 = Label(window, text=" ", background="white")                                                      #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

AccountNum = Label (window, text="Account Number:", font='Helvetica 10', background="white") #CREATING THE LABEL THAT WILL SAY 'Account Number' ABOVE THE ENTRY BOX
accountnum = Entry (window, background="light grey")                                         #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR ACCOUNT NUMBER, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
Username = Label (window, text="Username:", font='Helvetica 10', background="white")         #CREATING THE LABEL THAT WILL SAY 'Username' ABOVE THE ENTRY BOX
username = Entry (window, background="light grey")                                           #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR USERNAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
Password = Label (window, text="Password:", font='Helvetica 10', background="white")         #CREATING THE LABEL TAHT WILL SAY 'Password' ABOVE THE ENTRY BOX
password = Entry (window, background="light grey", show="*")                                 #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR PASSOWRD, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
S3 = Label(window, text=" ", background="white")                                             #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

Login = Button (text="      LOGIN      ", fg="green", command=Login)                         #CREATING THE LOGIN BUTTON 

S4 = Label(window, text=" ", background="white")                                                                                   #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
signup = Label (window, text="No Account? Why Don't You Sign Up Today By Clicking Below!", font='Helvetica 8', background="white") #CREATING A LABEL THAT STATES A USER CAN SIGN UP FOR AN ACCOUNT
SignUp = Button (text="     SIGN UP     ", fg="red", command=SignUp)                                                               #CREATING THE SIGN UP BUTTON 

Logo.pack()        #DISPLAYING THE LOGO LABEL
S1.pack()          #DISPLAYING THE SPACE LABEL
Title.pack()       #DISPLAYING THE TITLE OF THE WINDOW
S2.pack()          #DISPLAYING THE SPACE LABEL
AccountNum.pack()  #DISPLAYING THE ACCOUNT NUMBER LABEL THAT WILL SIT ABOVE THE ENTRY BOX
accountnum.pack()  #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR ACCOUNT NUMBER
Username.pack()    #DISPLAYING THE USERNAME LABEL THAT WILL SIT ABOVE THE ENTRY BOX
username.pack()    #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR USERNAME
Password.pack()    #DISPLAYING THE PASSWORD LABEL THAT WILL SIT ABOVE THE ENTRY BOX
password.pack()    #DISPLAYING THE ENTRY BOX FOR THE USER TO INPUT THEIR PASSWORD
S3.pack()          #DISPLAYING THE SPACE LABEL
Login.pack()       #DISPLAYING THE LOGIN BUTTON 
S4.pack()          #DISPLAYING THE SPACE LABEL
signup.pack()      #DISPLAYING THE SIGN UP MESSAGE
SignUp.pack()      #DISPLAYING THE SIGN UP BUTTON








#CMP9134M ADVANCED SOFTWARE ENGINEERING - LOGIN
#NATHAN JONES
#FEB/MAR 2023
