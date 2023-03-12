#CMP9134M ADVANCED SOFTWARE ENGINEERING - CMP BANKING SYSTEM
#NATHAN JONES
#FEB/MAR 2023

from tkinter import ttk                                          #IMPORTING THE TKK MODULE THAT ALLOWS FOR TABBED WIDGETS
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry  #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  #ALLOWING FOR THE MATPLOTLIB GRAPHS TO BE INSERTED INTO THE TKINTER GUI'S
from PIL import Image, ImageTk                                   #ALLOWS FOR THE IMPORTS OF IMAGES INTO THE PROGGRAM TO MAKE IT VISUALLY LOOK MORE PROFESSIONAL
from tkinter import *                                            #ALLOWS FOR THE REST OF THE TKINTER LIBARY TO BE IMPORTED
from uuid import getnode as get_mac                              #ALLOWS FOR TO ACCESS THE MODULES THAT ALLOW DIRECT ACCESS TO THE MAC ADDRESS OF THE MACHINE

import tkinter as tk                                             #IMPORTING THE TKINTER MODULE TO BE USED IN THE PROGRAM
import sys                                                       #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON
import os.path                                                   #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS
import os                                                        #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import matplotlib.pyplot as plt                                  #IMPORTING MATPLOTLIB SO THAT GRAPHS CAN BE CREATED AND PRODUCED IN THE PROGRAM
import pandas as pd                                              #ALLOWS FOR CERTIAN MATHMATICAL FUNCTIONS AND READING OF CSV DATA TO TAKE PLACE
import datetime                                                  #ALLOWS FOR THE USE OF CURRENT DATES AND TIMES TO BE ACCESSED
import socket                                                    #ALLOWS FOR THE PROGRAM TO GATHER SOCKET INFORMATION
import csv                                                       #ALLOWS FOR THE ACCESS OF THE CSV FILE FOR READING/WRITING AND APPENDING TO THE FILE

time = datetime.datetime.now()                       #GATHERING THE CURRENT TIME AND DATE
mac = get_mac()                                      #GATHERING THE CURRENT MAC ADDRESS OF THE MACHINE 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #GATHERING THE CURRENT IP ADDRESS 
s.connect(("8.8.8.8", 80))                           #CONNECTS TO THE IP ADDRESS AND ESTABLISHES THE CONNECTION

def MainMenu():
    
    Menu = Tk()                               #CREATING THE TKINTER WINDOW THAT WILL HOUSE THE GUI TABS FOR THE MAIN APPLICATION
    Menu.title("CMP Banking System")          #CREATING THE TITLE OF THE WINDOW 
    Menu.resizable(width=FALSE, height=FALSE) #MAKING IT SO THAT THE WINDOW CANNOT BE CHANGE IN SIZE AND WILL BE THE SAME SIZE ON ALL SYSTEMS 
    Menu.geometry("1400x700")                 #SETTING THE WINDOW TO BE A SPECIFIC GEOMETRY FOR ALL SYSTEMS
    tabControl = ttk.Notebook(Menu)           #MAKING THETKINTER WINDOW A NOTEBOOK SO THERE ARE TABS AT THE TOP AND THE USER CAN GO INBETWEEN TABS

    style = ttk.Style()                                                  #CREATING A VARIABLE CALLED STYLE THAT WILL BE CALLED LATER ON IN THE PROGRAM
    style.configure("W.TFrame", foreground="white", background="white")  #CONFIGURING THE STYLE OF THE APPLICATION TO HAVE A WHITE BACKGROUND AND FOREGROUND

    WelcomeTab = ttk.Frame(style="W.TFrame")                             #CREATING AND CONFIGURING THE WELCOME TAB TO HAVE THE WHITE COLOUR SCHEME 

    for line in open("temp.txt","r").readlines():   #READING EACH LINE WITHIN THE 'temp' FILE AND ASSIGNING THE DATA TO VARIABLES BELOW
        data = line.split()                         #SPLITTING THE TEXT UP INSIDE THE FILE SO THEY CAN BE ACCESSED AND ASSIGNED
        name = data[0]                              #TAKING THE 1ST ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'name' AS THIS IS THE USER'S NAME
        email = data[1]                             #TAKING THE 2ND ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'email' AS THIS IS THE USER'S EMAIL
        acc = data[2]                               #TAKING THE 3RD ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'acc' AS THIS IS THE USER'S ACCOUNT NUMBER AND WILL BE NEEDED LATER WHEN ACCESSING THE CORRECT ACCOUNT
        accname = data[3]                           #TAKING THE 4TH ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'accname' AS THIS IS THE USER'S ACCOUNT NUMBER AND WILL BE USED LATER 

    logo = PhotoImage(file="CMPBANKINGLOGO.png")    #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE MAIN BANKING SYSTEM TAB

    S = Label(WelcomeTab, text=" ", background="white")                                                                                #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
    Logo = Label (WelcomeTab, image=logo)                                                                                              #CREATING THE LABEL THAT WILL DISPLAY THE CMP BANKING LOGO AT THE TOP OF THE MAIN BANKING SYSTEM TAB
    S1 = Label(WelcomeTab, text=" ", background="white")                                                                               #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN 
    Time = Label(WelcomeTab, text="Current System Time: "+str(time.strftime("%Y-%m-%d %H:%M")), font='Helvetica 11 bold', bg="white")  #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP AND WILL DISPLAY THE CURRENT DATE-TIME OF THE SYSTEM
    S2 = Label(WelcomeTab, text=" ", background="white")                                                                               #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN 
    SubTitle = Label(WelcomeTab, text="Welcome To The CMP Banking System!", font='Helvetica 10 bold', bg="white")                      #CREATING A LABEL THAT WELCOMES THE USER TO THE SYSTEM 
    S3 = Label(WelcomeTab, text=" ", background="white")                                                                               #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN 
    
    WelcomeMsg = Label(WelcomeTab, text="Welcome " +str(name)+", please select the tab above for what area of your account you would like to see.", font='Helvetica 10', bg="white") #CREATING THE LABEL THAT ACTS AS A PERSONALISED WELCOME MESSAGE

    S.pack()           #DISPLAYING THE SPACE LABEL
    Logo.pack()        #DISPLAYING THE CMP BANKING SYSTEM LOGO
    S1.pack()          #DISPLAYING THE SPACE LABEL
    Time.pack()        #DISPLAYING THE CURRENT DATE AND TIME
    S2.pack()          #DISPLAYING THE SPACE LABEL
    SubTitle.pack()    #DISPLAYING THE SUBTITLE TO THE USER
    S3.pack()          #DISPLAYING THE SPACE LABEL
    WelcomeMsg.pack()  #DISPLAYING THE PERSONALISED WELCOME MESSAGE TO THE USER
    
    BalenceTab = ttk.Frame(style="W.TFrame") #CREATING AND CONFIGURING THE BALANCE TAB TO HAVE THE WHITE COLOUR SCHEME  
    file = "acc\\"+"\\"+str(acc)+".csv"      #TAKING THE USERS ACCOUNT NUMBER THAT HAS BEEN PASSED THROUGH FROM THE LOGIN PROGRAM TO THE MAIN PROGRAM, THIS ACCOUNT NUMBER IS THEN ADDED TO A STRING TO CREATE THE FILE PATH OF THE USERS ACCOUNT DETAILS

    def Balence():

        with open(file, "r") as f:                                                                               #READING THE CSV FILE THAT CONTAINS THE DATA 
            reader = csv.reader(f)                                                                               #CREATING THE VARIABLE THAT WILL READ THE DATA
            data = list(reader)                                                                                  #CREATING THE VARIABLE THAT WILL STORE THE DATA
        Last20Rows = data[-20:]                                                                                  #CREATING THE VARIABLE TAHT WILL HOLD THE LAST 20 ELEMENTS OF THE CSV
        Last15Table = tk.ttk.Treeview(BalenceTab, columns=list(range(len(data[0]))), show="headings", height=20) #CREATING THE TABLE WITH A  SPECIFIC HEIGHT OF 20 ROWS WHILST SHOWING THE HEADINGS OF EACH COLUMN
        for i, heading in enumerate(data[0]):                                                                    #FOR EACH COLUMN IN THE FILE THE FOLLOWING WILL TAKE PLACE
            Last15Table.heading(i, text=heading)                                                                 #DISPLAYING EACH HEADING FROM THE FILE TO THE TABLE
        for row in Last20Rows:                                                                                   #FOR EACH OF THE LAST 20 ROWS THE FOLLOWING TAKES PLACE
            Last15Table.insert("","end",values=row)                                                              #ASSIGN EACH ROW OF THE FILE TO THE TABLE SO IT WILL BE DISPLAYED

        S = Label(BalenceTab, text=" ", background="white")                                                #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        Title = Label(BalenceTab, text="Current Account Balance", font='Helvetica 14 bold', bg="white")    #CREATING THE SYSTEM DETAILS TITLE FOR THE TAB
        S1 = Label(BalenceTab, text=" ", background="white")                                               #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        Details = Label(BalenceTab,
                        text="Below is the current account balance of the "+str(acc)+" "+str(accname)+" Account, along with the transactions in the past 20 days.",
                        font='Helvetica 11', bg="white")                                                   #CREATING THE LABEL THAT ACTS AS A DESCRIPTION FOR THE TAB
        
        BalenceSheet = plt.Figure(figsize=(6,5),dpi=90)                                                    #CREATING THE FIGURE THAT WILL BE USED TO HOUSE THE GRAPH FOR THE BALANCE
        balsheet = pd.read_csv(file, encoding='ISO-8859-1', parse_dates=['Month'], index_col="Month")      #READING THE DATA FROM THE ACCOUNT THAT HAS BEEN GIVEN TO THE APPLICATION
        ax = BalenceSheet.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FIGURE AND TO THE TAB 
        BALSHEET = FigureCanvasTkAgg(BalenceSheet, BalenceTab)                                             #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE BALANCE OF THE ACCOUNT
        BALSHEET.get_tk_widget().place(x=120, y=100)                                                       #PLACING THE GRAPH WITHIN THE TAB OVER TO THE LEFT OF THE TAB
        
        Last15Table.place(x=820, y=120)                                                                    #PLACING THE TABLE WITHIN THE TAB LOCATED TO TEH RIGHT OF THE GRAPH
        
        ax.set_ylabel("Current Balence in £")                                                              #SETTING THE Y LABEL ON THE GRAPH TO BE "Current Balence in £"
        balsheet.plot(color='#d5d8dc', title='Current Balence Within The Account',ax=ax)                   #GIVING THE GRAPH A TITLE AND COLOUR SCHEME

        B1 = Button(BalenceTab, text="Refresh", command=Balence)                                           #CREATING A BUTTON THAT WILL REFRESH THE GRAPH

        S.pack()              #DISPLAYING THE SPACE LABEL
        Title.pack()          #DISPLAYING THE TITLE OF THE TAB
        S2.pack()             #DISPLAYING THE SPACE LABEL
        Details.              #DISPLAYING THE DESCRIPTION OF THE TAB
        B1.place(x=680, y=80) #PLACING THE BUTTON WITHIN THE TAB 

    Balence()                 #RUNNING THE FUNCTION SO IT IS ALREADY LOADED UP
    
    SysDetailsTab = ttk.Frame(style="W.TFrame") #CREATING AND CONFIGURING THE SYSTEM DETAILS TAB TO HAVE THE WHITE COLOUR SCHEME

    def SystemDetails():

        S = Label(SysDetailsTab, text=" ", background="white")                                                                                                            #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        Title = Label(SysDetailsTab, text="System Details", font='Helvetica 14 bold', bg="white")                                                                         #CREATING THE SYSTEM DETAILS TITLE FOR THE TAB
        S1 = Label(SysDetailsTab, text=" ", background="white")                                                                                                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        Details = Label(SysDetailsTab,
                        text="Below are the current details of the system you are accessing the CMP Banking System from, and are stored incase of FRAUDULENT ACTIVITY.",
                        font='Helvetica 11', bg="white")                                                                                                                  #CREATING THE LABEL THAT ACTS AS A DESCRIPTION FOR THE TAB
        S2 = Label(SysDetailsTab, text=" ", background="white")                                                                                                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        SysTime = Label(SysDetailsTab, text="Current System Time: "+str(time.strftime("%Y-%m-%d %H:%M")), font='Helvetica 10 bold', bg="white")                           #CREATING THE LABEL THAT DISPLAYS THE CURRETN SYSTEM TIME AND DATE
        CurEmail = Label(SysDetailsTab, text="Current Usename Logged In: "+str(email), font='Helvetica 10 bold', bg="white")                                              #CREATING THE LABEL THAT DISPLAYS THE USERNAME OF THE USER THATS LOGGED IN
        S3 = Label(SysDetailsTab, text=" ", background="white")                                                                                                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        SysIP = Label(SysDetailsTab, text="Current System IP Address:  "+str(s.getsockname()[0]), font='Helvetica 10 bold', bg="white")                                   #CREATING THE LABEL THAT DISPLAYS THE CURRENT IP ADDRESS OF THE MACHINE
        CurUsr = Label(SysDetailsTab, text="Current User Logged In: "+str(name), font='Helvetica 10 bold', bg="white")                                                    #CREATING THE LABEL THAT DISPLAYS THE USER'S NAME THAT IS LOGGED IN
        S4 = Label(SysDetailsTab, text=" ", background="white")                                                                                                           #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        SysMAC = Label(SysDetailsTab, text="Current System MAC Address: "+str(mac), font='Helvetica 10 bold', bg="white")                                                 #CREATING THE LABEL THAT DISPLAYS THE CURRENT MAC ADDRESS OF THE MACHINE
        CurACC = Label(SysDetailsTab, text="Current Account Logged In: "+str(acc), font='Helvetica 10 bold', bg="white")                                                  #CREATING THE LABEL THAT DISPLAYS THE ACCOUNT NUMBER THAT IS LOGGED IN

        S.pack()                     #DISPLAYING THE SPACE LABEL
        Title.pack()                 #DISPLAYING THE TITLE OF THE TAB
        S1.pack                      #DISPLAYING THE SPACE LABEL
        Details.pack()               #DISPLAYING THE DESCRIPTION OF THE TAB
        S2.pack()                    #DISPLAYING THE SPACE LABEL
        SysTime.place(x=225, y=100)  #DISPLAYING THE SYSTEM TIME
        CurEmail.place(x=800, y=100) #DISPLAYING THE USERNAME
        S3.pack()                    #DISPLAYING THE SPACE LABEL
        SysIP.place(x=225, y=150)    #DISPLAYING THE SYSTEM IP ADDRESS
        CurUsr.place(x=800, y=150)   #DISPLAYING THE USER'S NAME
        S4.pack()                    #DISPLAYING THE SPACE LABEL
        SysMAC.place(x=225, y=200)   #DISPLAYING THE CURRENT MAC ADDRESS
        CurACC.place(x=800, y=200)   #DISPLAYING THE CURRENT ACCOUNT NUMBER
        
    SystemDetails()                  #RUNNING THE FUNCTION SO IT IS ALREADY LOADED UP
    
    tabControl.add(WelcomeTab, text='Welcome Page')       #CREATING THE TAB AT THE TOP OF THE PAGES TO GO TO THE WELCOME PAGE TAB
    tabControl.add(BalenceTab, text='Balence Sheet')      #CREATING THE TAB AT THE TOP OF THE PAGES TO GO TO THE BALANCE SHEET TAB
    tabControl.add(SysDetailsTab, text='System Details')  #CREATING THE TAB AT THE TOP OF THE PAGES TO GO TO THE SYSTEM DETAILS TAB
    tabControl.pack(expand = 1, fill ="both")             #DISPLAYING THE TABS ALONG THE TOP
    
MainMenu()








#CMP9134M ADVANCED SOFTWARE ENGINEERING - CMP BANKING SYSTEM
#NATHAN JONES
#FEB/MAR 2023
