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
    
    Menu = Tk()                                      #CREATING THE TKINTER WINDOW THAT WILL HOUSE THE GUI TABS FOR THE MAIN APPLICATION
    logo = PhotoImage(file="CMPBANKINGLOGO.png")     #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE MAIN BANKING SYSTEM TAB
    Menu.iconphoto(False, logo)                      #SETTING THE CMP LOGO IN THE TOP BAR OF THE WINDOW
    Menu.title("CMP Banking System")                 #CREATING THE TITLE OF THE WINDOW 
    Menu.resizable(width=FALSE, height=FALSE)        #MAKING IT SO THAT THE WINDOW CANNOT BE CHANGE IN SIZE AND WILL BE THE SAME SIZE ON ALL SYSTEMS 
    Menu.geometry("1400x700")                        #SETTING THE WINDOW TO BE A SPECIFIC GEOMETRY FOR ALL SYSTEMS
    tabControl = ttk.Notebook(Menu)                  #MAKING THETKINTER WINDOW A NOTEBOOK SO THERE ARE TABS AT THE TOP AND THE USER CAN GO INBETWEEN TABS

    style = ttk.Style()                                                  #CREATING A VARIABLE CALLED STYLE THAT WILL BE CALLED LATER ON IN THE PROGRAM
    style.configure("W.TFrame", foreground="white", background="white")  #CONFIGURING THE STYLE OF THE APPLICATION TO HAVE A WHITE BACKGROUND AND FOREGROUND

    WelcomeTab = ttk.Frame(style="W.TFrame")                             #CREATING AND CONFIGURING THE WELCOME TAB TO HAVE THE WHITE COLOUR SCHEME 

    for line in open("temp.txt","r").readlines():   #READING EACH LINE WITHIN THE 'temp' FILE AND ASSIGNING THE DATA TO VARIABLES BELOW
        data = line.split()                         #SPLITTING THE TEXT UP INSIDE THE FILE SO THEY CAN BE ACCESSED AND ASSIGNED
        name = data[0]                              #TAKING THE 1ST ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'name' AS THIS IS THE USER'S NAME
        email = data[1]                             #TAKING THE 2ND ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'email' AS THIS IS THE USER'S EMAIL
        acc = data[2]                               #TAKING THE 3RD ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'acc' AS THIS IS THE USER'S ACCOUNT NUMBER AND WILL BE NEEDED LATER WHEN ACCESSING THE CORRECT ACCOUNT
        accname = data[3]                           #TAKING THE 4TH ELEMENT OF THE FILE AND APPENDNING IT TO THE VARIABLE 'accname' AS THIS IS THE USER'S ACCOUNT NUMBER AND WILL BE USED LATER 

    S = Label(WelcomeTab, text=" ", background="white")                                                                                #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
    Logo = Label (WelcomeTab, image=logo)                                                                                              #CREATING THE LABEL THAT WILL DISPLAY THE CMP BANKING LOGO AT THE TOP OF THE MAIN BANKING SYSTEM TAB
    S1 = Label(WelcomeTab, text=" ", background="white")                                                                               #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN 
    Time = Label(WelcomeTab, text="Current System Time: "+str(time.strftime("%Y-%m-%d %H:%M")), font='Helvetica 11 bold', bg="white")  #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP AND WILL DISPLAY THE CURRENT DATE-TIME OF THE SYSTEM
    S2 = Label(WelcomeTab, text=" ", background="white")                                                                               #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN 
    SubTitle = Label(WelcomeTab, text="Welcome To The CMP Banking System!", font='Helvetica 10 bold', bg="white")                      #CREATING A LABEL THAT WELCOMES THE USER TO THE SYSTEM 
    S3 = Label(WelcomeTab, text=" ", background="white")                                                                               #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN 
    
    WelcomeMsg = Label(WelcomeTab, text="Welcome " +str(name)+", please select the tab above for what area of your account you would like to see.", font='Helvetica 10', bg="white") #CREATING THE LABEL THAT ACTS AS A PERSONALISED WELCOME MESSAGE

    def LogOut():

        messagebox.showinfo("logged out", "You Are Logged Out!")      #DISPLAYS A MESSAGE TO THE USER STATING THEY HAVE LOGGED IN
        with open("temp.txt", "w") as file:                           #WITH THE TEMP FILE OPEN THE FOLLOWING WILL BE WRITTEN TO TEMP FILE - BY WRITING A SPACE IT WILL CLEAR THE TEMP FILE SO ITS BLANK FOR THE NEXT LOG IN
                file.write(" ")                                       #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
                file.close()                                          #CLOSING THE FILE AFTER ALL OF THE DATA HAS BEEN WRITTEN TO THE TEMP FILE 
        Menu.destroy()                                                #CLOSING THE MAIN WINDOW AFTER A SUCCESSFUL LOG OUT
    
    LogOutButton = Button(WelcomeTab, text="Log Out", command=LogOut) #CREATING THE LOG OUT BUTTON THAT IS ON THE WELCOME PAGE SO THAT THE USER CAN LOG OUT WHEN THEY ARE DONE

    S.pack()                            #DISPLAYING THE SPACE LABEL
    Logo.pack()                         #DISPLAYING THE CMP BANKING SYSTEM LOGO
    S1.pack()                           #DISPLAYING THE SPACE LABEL
    Time.pack()                         #DISPLAYING THE CURRENT DATE AND TIME
    S2.pack()                           #DISPLAYING THE SPACE LABEL
    SubTitle.pack()                     #DISPLAYING THE SUBTITLE TO THE USER
    S3.pack()                           #DISPLAYING THE SPACE LABEL
    WelcomeMsg.pack()                   #DISPLAYING THE PERSONALISED WELCOME MESSAGE TO THE USER
    LogOutButton.place(x=1300, y=625)   #PLACING THE LOG OUT BUTTON IN THE BOTTOM LEFT OF THE TAB
    
    BalenceTab = ttk.Frame(style="W.TFrame") #CREATING AND CONFIGURING THE BALANCE TAB TO HAVE THE WHITE COLOUR SCHEME  
    file = "acc\\"+"\\"+str(acc)+".csv"      #TAKING THE USERS ACCOUNT NUMBER THAT HAS BEEN PASSED THROUGH FROM THE LOGIN TO THE MAIN, THIS ACCOUNT NUMBER IS THEN ADDED TO A STRING TO CREATE THE FILE PATH OF THE USERS ACCOUNT DETAILS

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

        S = Label(BalenceTab, text=" ", background="white")                                                      #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        Title = Label(BalenceTab, text="Current Account Balance", font='Helvetica 14 bold', bg="white")          #CREATING THE SYSTEM DETAILS TITLE FOR THE TAB
        S1 = Label(BalenceTab, text=" ", background="white")                                                     #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE INBETWEEN
        Details = Label(BalenceTab,
                        text="Below is the current account balance of the "+str(acc)+" "+str(accname)+" Account, along with the 20 past transactions.",
                        font='Helvetica 11', bg="white")                                                         #CREATING THE LABEL THAT ACTS AS A DESCRIPTION FOR THE TAB
        
        BalenceSheet = plt.Figure(figsize=(6,5),dpi=90)                                                          #CREATING THE FIGURE THAT WILL BE USED TO HOUSE THE GRAPH FOR THE BALANCE
        balsheet = pd.read_csv(file, encoding='ISO-8859-1', parse_dates=['Month'], index_col="Month")            #READING THE DATA FROM THE ACCOUNT THAT HAS BEEN GIVEN TO THE APPLICATION
        ax = BalenceSheet.add_subplot(111)                                                                       #ADDING THE GRAPH TO THE FIGURE AND TO THE TAB 
        BALSHEET = FigureCanvasTkAgg(BalenceSheet, BalenceTab)                                                   #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE BALANCE OF THE ACCOUNT
        BALSHEET.get_tk_widget().place(x=120, y=100)                                                             #PLACING THE GRAPH WITHIN THE TAB OVER TO THE LEFT OF THE TAB
        
        Last15Table.place(x=820, y=120)                                                                          #PLACING THE TABLE WITHIN THE TAB LOCATED TO TEH RIGHT OF THE GRAPH
        
        ax.set_ylabel("Current Balence in £")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "Current Balence in £"
        balsheet.plot(color='#d5d8dc', title='Current Balence Within The Account',ax=ax)                         #GIVING THE GRAPH A TITLE AND COLOUR SCHEME

        B1 = Button(BalenceTab, text="Refresh", command=Balence)                                                 #CREATING A BUTTON THAT WILL REFRESH THE GRAPH

        S.pack()                    #DISPLAYING THE SPACE LABEL
        Title.place(x=600, y=20)    #DISPLAYING THE TITLE OF THE TAB
        S2.pack()                   #DISPLAYING THE SPACE LABEL
        Details.place(x=400, y=50)  #DISPLAYING THE DESCRIPTION OF THE TAB
        B1.place(x=680, y=80)       #PLACING THE BUTTON WITHIN THE TAB 

    Balence()                 #RUNNING THE FUNCTION SO IT IS ALREADY LOADED UP

    DepositWithdrawTab = ttk.Frame(style="W.TFrame") #CREATING AND CONFIGURING THE DEPOSIT/WITHDRAW TAB TO HAVE THE WHITE COLOUR SCHEME 
    
    def DepositWithdraw():

        def AUTH():

             DIGITS = int(auth.get())   #GATHERING THE 16-DIGIT CREDIT CARD NUMBER FROM THE ENTRY BOX
             
             if not LENcheck(DIGITS):                                                                   #IF THE CARD NUMBER'S DOES NOT EQUAL 16 THEN THE FOLLOWING WILL HAPPEN
                 messagebox.showinfo("   ERROR!   ", "INVALID CREDIT CARD NUMBER LENGTH", icon="error") #DISPLAYING THE ERROR MESSAGE BOX INVALID CARD MESSAGE
             else:                                                                                      #IF THE CARD'S NUMBER HAS 16 DIGITS THEN THE FOLLOWING WILL HAPPEN 
                if not valid(DIGITS):                                                                   #IF THE CARD NUMBER'S FINAL SUM DOES NOT EQUAL 0 THEN THE FOLLOWING WILL HAPPEN      
                    messagebox.showinfo("   ERROR!   ", "INVALID CREDIT CARD NUMBER", icon="error")     #DISPLAYING THE ERROR MESSAGE BOX WITH INVALID CARD MESSAGE 
                if valid(DIGITS):                                                                       #IF THE CARD NUMBER'S FINAL SUM EQUALS 0 THEN THE FOLLOWING WILL HAPPEN    
                    messagebox.showinfo("Deposit", "Deposit Made!")                                     #DISPLAYING THE DEPOSIT MESSAGE SO THE USER KNOWS THEY HAVE MADE THEIR DEPOSIT
                    DepositFunc()                                                                       #RUNNING THE DEPOSIT FUCTION SO THAT FUNDS ARE ACTUALLY ADDED TO THE ACCOUNT
        
        def LENcheck(DIGITS):                    #THIS FUNCTION WILL CHECK THE LENGTH OF THE DIGITS TO MAKE SURE THEY ARE EQUAL TO 16
            length = len(str((DIGITS)))          #DEFINING WHAT 'length' WILL BE AND IN THIS CASE IT IS THE DIGITS THAT HAVE BEEN ENTERED BY THE USER 
            if (length == 16):                   #IF THE VALUE OF 'length' IS EQUAL TO 16 THEN THE FOLLOWING WILL TAKE PLACE  
              return True                        #IT WILL RETURN THE VALUE OF TRUE SO THAT THE PROGRAM CAN THEN BEGIN THE CALCULATIONS 
            else:                                #IF THE VALUE OF 'length' IS NOT EQUAL TO 16 THEN THE FOLLOWING WILL TAKE PLACE 
              return False                       #IT WILL RETURN THE VALUE OF FALSE SO THAT THE PROGRAM WILL NOT COMPLETE ANY CALCULATIONS, RATHER IT WILL DISPLAY THE NOT VALID MESSAGE

        def valid(DIGITS):                       #THIS IS THE FUNCTION THAT WILL COMPLETE THE CALCULATIONS TO SEE IF THE CARD NUMBER IS A VALID ONE 
            card = DIGITS                        #TAKING THE DIGITS THE USER HAS ENTERED AND NOW ASSIGNING THE DIGITTS TO A NEW VARIABLE 
            Digits = list((str(card)))           #THE VARIABLE THAT WAS CREATED ABOVE IS NOW BEING ASSIGNED AS A LIST AND STRING OF NUMBERS IN ANOTHER VARIABLE
            oddSUM = 0                           #SETTING THE VALUE OF 'oddSUM' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
            evenSUM = 0                          #SETTING THE VALUE OF 'evenSUM' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
            EVENcount = 0                        #SETTING THE VALUE OF 'EVENcount' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
            ODDcount = 0                         #SETTING THE VALUE OF 'ODDcount' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
            totalSUM = 0                         #SETTING THE VALUE OF 'totalSUM' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
            length = 0                           #SETTING THE VALUE OF 'length' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
            for i in Digits:             
              length += 1                        #CHANGING THE 'length' VARIABLE TO CREATE A COUNT THAT WILL ADD ONE FOR EACH DIGIT - THIS WILL KEEP TRACK OF THE LENGTH OF THE CARD NUMBER    
            count = 0                            #BUT KEEPING THE COUNT AS 0 SO THAT THE PROGRAM CAN KEEP TRACK 
            if length == 16:             
              ODDcount = 15                      #CHANGING THE 'ODDcount' TO REPRESENT NEW COUNT FOR THE ODD DIGITS
              EVENcount = 14                     #CHANGING THE 'EVENcount' TO REPRESENT NEW COUNT FOR THE EVEN DIGITS
            if length == 15:             
              ODDcount = 13                      #CHANGING THE 'ODDcount' TO REPRESENT NEW COUNT FOR THE ODD DIGITS
              EVENcount = 14                     #CHANGING THE 'EVENcount' TO REPRESENT NEW COUNT FOR THE EVEN DIGITS 

            while (count <= length-2):           #WHILE THE 'count' VARIABLE IS LOWER OR EQUAL TO THE 'length' VARIABLE BUT MINUS 2 THEN THE FOLLOWING WILL TAKE PLACE

              evenSUM += int(Digits[EVENcount])  #TAKING THE 'evenSUM' AND ADDING IT TO THE DIGITS AND 'EVENcount' 
              EVENcount -= 2                     #UPDATING THE 'EVENcount'   
              
              prod = 2 * int(Digits[ODDcount])   #CREATING A VARIABLE THAT IS 2 TIMES THE DIGITS AND 'ODDcount'
              oddSUM += prod                     #UPDATING THE 'oddSUM' WITH THE 'prod' VARIABLE BY ADDING IT 
              ODDcount -= 2                      #UPDATING THE 'ODDcount' TO BE WHATEVER IT IS MINUS 2   
              count += 2                         #UPDATING THE 'count' TO BE WHATEVER IT IS PLUS 2

            totalSUM = oddSUM + evenSUM          #THE FINAL OR 'totalSUM' IS MADE UP OF ADDING THE 'oddSUM' AND 'evenSUM' TOGETHER TO CREATE THE FINAL SUM  

            if totalSUM % 10 == 0:               #IF THE FINAL SUM CAN BE DIVIDED BY 10 THEN THE FOLLOWING WILL TAKE PLACE  
              return True                        #RETURNING THE TRUE VALUE SO THAT THE PROGRAM CAN DISPLAY THE VALID CARD MESSAGE
            else:                                #IF THE FINAL SUM CANNOT BE DIVIDED BY 10 THEN THE FOLLOWING WILL TAKE PLACE 
              return False                       #RETURNING THE FALSE VALUE SO THAT THE PROGRAM CAN DISPLAY THE INVALID CARD MESSAGE        

        def DepositFunc():

            DateDep = time.strftime("%d-%b") #GATHERING THE CURRENT DATE IN A FORMAT LIKE THIS "10-Mar"
            Int_Dep = int(deposit.get())     #CONVERTING THE DEPOSIT AMOUNT FROM THE ENTRY TO AN INT
            Int_Data = int(data[-1])         #CONVERTING THE BALANCE FROM WITHIN THE FILE TO BE AN INT
            NewBal = Int_Data + Int_Dep      #CALCULATING THE NEW BALANCE BY ADDING THE DEPOSIT AMOUNT TO THE BALANCE
            
            with open(file, "a") as f:       #WHILST THE FILE IS OPEN THE FOLLOWING WILL BE APPENED TO IT
                f.write("\n")                #STARTING ON A NEW LINE SO THAT THE PREVIOUS TRANSACTIONS DO NOT GET MIXED UP
                f.write(DateDep)             #WRITING THE CURRENT DATE TO THE ACCOUNT SO THE USER CAN SEE WHEN THEY DEPOSITED TO THE ACCOUNT  
                f.write(",")                 #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
                f.write(str(NewBal))         #WRITING THE NEW BALANCE TO THE ACCOUNT    
                f.close()                    #CLOSING THE FILE ONCE THE DATA HAS BEEN APPENEDED TO THE ACCOUNT
                
            DepositWithdraw()                #RELOADING THE MAIN TAB SO THE NEW BALANCE IS DISPLAYED

        def WithdrawFunc():

            DateWit = time.strftime("%d-%b") #GATHERING THE CURRENT DATE IN A FORMAT LIKE THIS "10-Mar"
            Int_Wit = int(withdraw.get())    #CONVERTING THE WITHDRAW AMOUNT FROM THE ENTRY TO AN INT
            Int_Data = int(data[-1])         #CONVERTING THE BALANCE FROM WITHIN THE FILE TO BE AN INT
            NewBal = Int_Data - Int_Wit      #CALCULATING THE NEW BALANCE BY TAKING AWAY THE WITHDRAW AMOUNT FROM THE BALANCE

            with open(file, "a") as f:       #WHILST THE FILE IS OPEN THE FOLLOWING WILL BE APPENED TO IT
                f.write("\n")                #STARTING ON A NEW LINE SO THAT THE PREVIOUS TRANSACTIONS DO NOT GET MIXED UP
                f.write(DateWit)             #WRITING THE CURRENT DATE TO THE ACCOUNT SO THE USER CAN SEE WHEN THEY WITHDREW FROM THE ACCOUNT 
                f.write(",")                 #WRITING A COMMA BETWEEN THE TWO ENTRIES AS THE FILE HAS A CSV FORMAT
                f.write(str(NewBal))         #WRITING THE NEW BALANCE TO THE ACCOUNT  
                f.close()                    #CLOSING THE FILE ONCE THE DATA HAS BEEN APPENEDED TO THE ACCOUNT
                
            DepositWithdraw()                #RELOADING THE MAIN TAB SO THE NEW BALANCE IS DISPLAYED

        def TransferFunc():

            transaccnum = transferacc.get()                  #GETTING THE ACCOUNT NUMBER THE USER HAS ENTERED FOR THE 
            TransFile = "acc\\"+"\\"+str(transaccnum)+".csv" #TAKING THE USERS TRANSFER ACCOUNT NUMBER THAT HAS BEEN PASSED THROUGH, THIS NUMBER IS THEN ADDED TO A STRING TO CREATE THE FILE PATH OF THE TRANSFER ACCOUNT DETAILS
            for line in open(TransFile,"r").readlines():     #READING EACH LINE WITHIN THE 'temp' FILE AND ASSIGNING THE DATA TO VARIABLES BELOW
                tranacc = line.split(',')                    #SPLITTING THE TEXT UP INSIDE THE FILE SO THEY CAN BE ACCESSED AND ASSIGNED: #READING THE CSV FILE THAT CONTAINS THE DATA 
            TransLastBal = tranacc[-1]                       #GETTING THE LATEST BALANCE FROM THE ACCOUNT BY TAKING THE -1 OR LAST ELEMENT OF THE FILE
        
            DatetTans = time.strftime("%d-%b") #GATHERING THE CURRENT DATE IN A FORMAT LIKE THIS "10-Mar"
            Int_Trans = int(transfer.get())    #CONVERTING THE WITHDRAW AMOUNT FROM THE ENTRY TO AN INT
            Int_Data = int(data[-1])           #CONVERTING THE BALANCE FROM WITHIN THE FILE TO BE AN INT
            NewBal = Int_Data - Int_Trans      #CALCULATING THE NEW BALANCE BY TAKING AWAY THE TRANSFERED AMOUNT FROM THE BALANCE

            TransBal = int(TransLastBal) + int(transfer.get())      #CALCULATING THE NEW BALANCE BY ADDING THE TRANSFER AMOUNT TO THE BALANCE

            with open(file, "a") as f:       #WHILST THE FILE IS OPEN THE FOLLOWING WILL BE APPENED TO IT
                f.write("\n")                #STARTING ON A NEW LINE SO THAT THE PREVIOUS TRANSACTIONS DO NOT GET MIXED UP
                f.write(DatetTans)           #WRITING THE CURRENT DATE TO THE ACCOUNT SO THE USER CAN SEE WHEN THEY TRANSFERED FROM THE ACCOUNT 
                f.write(",")                 #WRITING A COMMA BETWEEN THE TWO ENTRIES AS THE FILE HAS A CSV FORMAT
                f.write(str(NewBal))         #WRITING THE NEW BALANCE TO THE ACCOUNT  
                f.close()                    #CLOSING THE FILE ONCE THE DATA HAS BEEN APPENEDED TO THE ACCOUNT

            with open(TransFile, "a") as t:  #WHILST THE FILE IS OPEN THE FOLLOWING WILL BE APPENED TO IT
                t.write("\n")                #STARTING ON A NEW LINE SO THAT THE PREVIOUS TRANSACTIONS DO NOT GET MIXED UP
                t.write(DatetTans)           #WRITING THE CURRENT DATE TO THE ACCOUNT SO THE USER CAN SEE WHEN THEY TRANSFERED TO THE ACCOUNT 
                t.write(",")                 #WRITING A COMMA BETWEEN THE TWO ENTRIES AS THE FILE HAS A CSV FORMAT
                t.write(str(TransBal))       #WRITING THE NEW BALANCE TO THE ACCOUNT  
                t.close()                    #CLOSING THE FILE ONCE THE DATA HAS BEEN APPENEDED TO THE ACCOUNT

            DepositWithdraw()                #RELOADING THE MAIN TAB SO THE NEW BALANCE IS DISPLAYED
            
        for line in open(file,"r").readlines():   #READING EACH LINE WITHIN THE 'temp' FILE AND ASSIGNING THE DATA TO VARIABLES BELOW
            data = line.split(',')                #SPLITTING THE TEXT UP INSIDE THE FILE SO THEY CAN BE ACCESSED AND ASSIGNED: #READING THE CSV FILE THAT CONTAINS THE DATA 
        LastBal = data[-1]                        #GETTING THE LATEST BALANCE FROM THE ACCOUNT BY TAKING THE -1 OR LAST ELEMENT OF THE FILE
        
        Title = Label(DepositWithdrawTab, text="Deposit or Withdraw", font='Helvetica 14 bold', bg="white")                   #CREATING THE DEPOSIT OR WITHDRAW TITLE FOR THE TAB
        Descp = Label(DepositWithdrawTab,
                     text="Welcome to the Deposit or Withdraw section of the CMP Banking System. Here you can choose to Deposit to or Withdraw from your account.",
                     font='Helvetica 11', bg="white")                                                                         #CREATING THE DESCRIPTION OF THE TAB THAT WILL GO UNDERNEATH THE TITLE
        CurBalDep = Label(DepositWithdrawTab, text="Current Balance: £"+str(LastBal), font='Helvetica 11 bold', bg="white")   #CREATING THE LABEL THAT SHOWS THE USER THE CURRETN BALANCE WITHIN THE ACCOUNT
        Deposit = Label(DepositWithdrawTab, text="Enter How Much You Would Like To Deposit", bg="white")                      #CREATING THE LABEL THAT ASKS THE USER HOW MUCH THEY WANT TO DEPOSIT 
        deposit = Entry(DepositWithdrawTab, background="light grey")                                                          #CREATING THE ENTRY BOX FOR THE USER TO ENTER THE AMOUNT THEY WANT TO DEPOSIT
        CardAuth = Label(DepositWithdrawTab, text="Enter Your Card Number" , bg="white") #USE 4007702835532454 FOR TESTING    #CREATING THE LABEL THAT ASKS THE USER TO ENTER THEIR CARD NUMBER
        auth = Entry(DepositWithdrawTab, background="light grey")                                                             #CREATING THE ENTRY BOX FOR THE USER TO ENTER THE CARD NUMBER
        DepositButton = Button(DepositWithdrawTab, text="Deposit", command=AUTH)                                              #CREATING THE BUTTON THAT WILL RUN THE FUNCTION THAT WILL ACTUALLY CHECK THE CARD AND DEPOSIT THE AMOUNT
        
        CurBalWit = Label(DepositWithdrawTab, text="Current Balance: £"+str(LastBal), font='Helvetica 11 bold', bg="white")   #CREATING THE LABEL THAT SHOWS THE USER THE CURRETN BALANCE WITHIN THE ACCOUNT
        Withdraw = Label(DepositWithdrawTab, text="Enter How Much You Would Like To Withdraw", bg="white")                    #CREATING THE LABEL THAT ASKS THE USER HOW MUCH THEY WANT TO WITHDRAW 
        withdraw = Entry(DepositWithdrawTab, background="light grey")                                                         #CREATING THE ENTRY BOX FOR THE USER TO ENTER THE AMOUNT THEY WANT TO WITHDRAW
        WithdrawButton = Button(DepositWithdrawTab, text="Withdraw", command=WithdrawFunc)                                    #CREATING THE BUTTON THAT WILL RUN THE FUNCTION THAT WILL ACTUALLY WITHDRAW THE AMOUNT

        CurBalTra = Label(DepositWithdrawTab, text="Current Balance: £"+str(LastBal), font='Helvetica 11 bold', bg="white")   #CREATING THE LABEL THAT SHOWS THE USER THE CURRETN BALANCE WITHIN THE ACCOUNT
        Transfer = Label(DepositWithdrawTab, text="Enter How Much You Would Like To Transfer", bg="white")                    #CREATING THE LABEL THAT ASKS THE USER HOW MUCH THEY WANT TO TRANSFER 
        transfer = Entry(DepositWithdrawTab, background="light grey")                                                         #CREATING THE ENTRY BOX FOR THE USER TO ENTER THE AMOUNT THEY WANT TO TRANSFER
        TransferACC = Label(DepositWithdrawTab, text="Enter The Account Number You Would Like To Transfer To", bg="white")    #CREATING THE LABEL THAT ASKS THE USER THE ACCOUNT THEY WANT TO TRANSFER TO
        transferacc = Entry(DepositWithdrawTab, background="light grey")                                                      #CREATING THE ENTRY BOX FOR THE USER TO ENTER THE ACCOUNT THEY WANT TO TRANSFER TO
        TransferButton = Button(DepositWithdrawTab, text="Transfer", command=TransferFunc)                                    #CREATING THE BUTTON THAT WILL RUN THE FUNCTION THAT WILL ACTUALLY TRANSFER THE AMOUNT
         
        Title.place(x=600, y=20)            #DISPLAYING THE TITLE OF THE TAB
        Descp.place(x=200, y=50)            #DISPLAYING THE DESCRIPTION OF THE TAB UNDERNEATH THE TITLE
        CurBalDep.place(x=120, y=100)       #DISPLAYING THE CURRENT BALANCE OF THE ACCOUNT
        Deposit.place(x=120, y=120)         #DISPLAYING THE LABEL THAT ASKS THE USER HOW MUCH THEY WANT TO DEPOSIT
        deposit.place(x=122, y=145)         #DISPLAYING THE ENTRY BOX FOR THE DEPOSIT AMOUNT
        CardAuth.place(x=120, y=160)        #DISPLAYING THE CARD NUMBER LABEL
        auth.place(x=122, y=185)            #DISPLAYING THE CARD NUMBER ENTRY BOX
        DepositButton.place(x=280, y=180)   #DISPLAYING THE BUTTON USED TO DEPOSIT THE MONEY
        CurBalWit.place(x=920, y=100)       #DISPLAYING THE CURRENT BALANCE OF THE ACCOUNT
        Withdraw.place(x=920, y=120)        #DISPLAYING THE LABEL THAT ASKS THE USER HOW MUCH THEY WANT TO WITHDRAW
        withdraw.place(x=922, y=145)        #DISPLAYING THE ENTRY BOX FOR THE WITHDRAW AMOUNT
        WithdrawButton.place(x=1080, y=140) #DISPLAYING THE BUTTON USED TO WITHDRAW THE MONEY
        CurBalTra.place(x=920, y=200)       #DISPLAYING THE CURRENT BALANCE OF THE ACCOUNT
        Transfer.place(x=920, y=220)        #DISPLAYING THE LABEL THAT ASKS THE USER HOW MUCH THEY WANT TO TRANSFER
        transfer.place(x=922, y=245)        #DISPLAYING THE ENTRY BOX FOR THE TRANSFER AMOUNT
        TransferACC.place(x=920, y=260)     #DISPLAYING THE LABEL THAT ASKS THE USER THE ACCOUNT THEY WANT TO TRANSFER TO
        transferacc.place(x=922, y=285)     #DISPLAYING THE ENTRY BOX FOR THE ACCOUNT NUMBER
        TransferButton.place(x=1080, y=280) #DISPLAYING THE BUTTON USED TO TRANSFER THE MONEY

    DepositWithdraw()  #RUNNING THE FUNCTION SO IT IS ALREADY LOADED UP
    
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
        S1.pack()                    #DISPLAYING THE SPACE LABEL
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
        
    tabControl.add(WelcomeTab, text='Welcome Page')             #CREATING THE TAB AT THE TOP OF THE PAGES TO GO TO THE WELCOME PAGE TAB
    tabControl.add(BalenceTab, text='Balence Sheet')            #CREATING THE TAB AT THE TOP OF THE PAGES TO GO TO THE BALANCE SHEET TAB
    tabControl.add(DepositWithdrawTab, text='Deposit/Withdraw') #CREATING THE TAB AT THE TOP OF THE PAGES TO GO TO THE Deposit/Withdraw TAB
    tabControl.add(SysDetailsTab, text='System Details')        #CREATING THE TAB AT THE TOP OF THE PAGES TO GO TO THE SYSTEM DETAILS TAB
    tabControl.pack(expand = 1, fill ="both")                   #DISPLAYING THE TABS ALONG THE TOP

# SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #  # SIGN UP WINDOW #

def SignUpApp():

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
            signupwin.destroy()                                                  #CLOSING THE SIGN UP WINDOW AS THE LOGIN WINDOW OPENS
            Login()                                                              #ONCE 'OK' HAS BEEN CLICKED THE LOGIN APPLICATION WILL BE STARTED

    signupwin = Tk()                                 #DEFINING WHAT THE TKINTER WINDOW WILL BE DEFINED AS
    logo = PhotoImage(file="CMPBANKINGLOGO.png")     #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE LOGIN WINDOW
    Logo = Label (signupwin, image=logo)             #CREATING THE LABEL THAT WILL DISPLAY THE CMP BANKING LOGO AT THE TOP OF THE LOGIN WINDOW
    signupwin.iconphoto(False, logo)                 #SETTING THE CMP LOGO IN THE TOP BAR OF THE WINDOW
    signupwin.resizable(0,0)                         #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    signupwin.resizable(width=FALSE, height=FALSE)   #THE USER CANNOT CHANGE THE SIZE OF THE LOGIN WINDOW
    signupwin.title ("CMP BANKING SYSTEM SIGN UP")   #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
    signupwin.geometry("500x700")                    #CONFIGURING THE FIXED SIZE OF THE LOGIN WINDOW WHICH WILL ALWAYS BE THIS SIZE            
    signupwin.configure(background='white')          #CONFIGURING THE BACKGROUND OF THE LOGIN WINDOW TO BE WHITE

    S1 = Label(signupwin, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
    Title = Label (signupwin, text="CMP BANKING SYSTEM SIGN UP", font='Helvetica 16 bold', background="white") #CREATING A TITLE FOR THE LOGIN WINDOW
    S2 = Label(signupwin, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

    FName = Label (signupwin, text="Enter First Name:", font='Helvetica 10', background="white")               #CREATING THE LABEL THAT WILL SAY FIRST NAME ABOVE THE ENTRY BOX
    fname = Entry (signupwin, background="light grey")                                                         #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR FIRST NAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
    SName = Label (signupwin, text="Enter Last Name:", font='Helvetica 10', background="white")                #CREATING THE LABEL THAT WILL SAY LAST NAME ABOVE THE ENTRY BOX
    sname = Entry (signupwin, background="light grey")                                                         #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR LAST NAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
    DOB = Label (signupwin, text="Enter Date of Birth:", font='Helvetica 10', background="white")              #CREATING THE LABEL THAT WILL SAY DOB ABOVE THE ENTRY BOX
    dob = Entry (signupwin, background="light grey")                                                           #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR DOB, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
    Username = Label (signupwin, text="Create Username:", font='Helvetica 10', background="white")             #CREATING THE LABEL THAT WILL SAY 'Username' ABOVE THE ENTRY BOX
    username = Entry (signupwin, background="light grey")                                                      #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR USERNAME, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
    Password = Label (signupwin, text="Create Password:", font='Helvetica 10', background="white")             #CREATING THE LABEL TAHT WILL SAY 'Password' ABOVE THE ENTRY BOX
    password = Entry (signupwin, background="light grey", show="*")                                            #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR PASSOWRD, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX 
    ACCNUM = Label (signupwin, text="Enter Account Number:", font='Helvetica 10', background="white")          #CREATING THE LABEL THAT WILL SAY DOB ABOVE THE ENTRY BOX
    accnum = Entry (signupwin, background="light grey")                                                        #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR DOB, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX
    ACCNAME = Label (signupwin, text="Enter Account Name:", font='Helvetica 10', background="white")           #CREATING THE LABEL THAT WILL SAY DOB ABOVE THE ENTRY BOX
    accname = Entry (signupwin, background="light grey")                                                       #CREATING AN ENTRY BOX WHERE THE USER WILL INPUT THEIR DOB, IT WILL HAVE A LIGHT GREY BACKGROUND WITHIN THE BOX

    S3 = Label(signupwin, text=" ", background="white")                                                        #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 

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

# LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #    # LOGIN WINDOW #

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
                file.write(" ")                                         #WRITING AN EMPTY SPACE BETWEEN THE USERS ENTRIES IN THE DATA FILE
                file.write(accname)                                     #GETTING THE USERS ACCOUNT NAME ASSOCIATED WITH THE ACCOUNT AND WRTITING IT TO THE TEMP FILE
                file.close()                                            #CLOSING THE FILE AFTER ALL OF THE DATA HAS BEEN WRITTEN TO THE TEMP FILE                                
            window.destroy()                                            #DESTROYS THE LOGIN WINDOW BEFORE OPENING THE MAIN APPLICATION
            MainMenu()                                                  #STARTING THE MAIN BANKING PROGRAM WITH THE USERS CREDENTIALS
            
        elif uname != data[0] or pword != data[1] or accnum != data[4]: #IF THE USERNAME AND/OR PASSWORD DO NOT MATCH ANY OF THE USERNAME/PASSWORD SET THE FOLLOWING STATEMENTS WILL COME INTO PLAY
            if trys == 0:                                                                                        #IF THE USER HAS 0 TRYS LEFT THEN THE FOLLOWING WILL TAKE PLACE
                messagebox.showinfo("   ERROR!   ", """  Your username and/or password was incorrect!                                                        
                You have """+str(trys)+str(" attempts left! And Have been LOCKED OUT!") , icon="error")          #DISPLAYING THE ERROR MESSAGE BOX STATING THEY HAVE BEEN LOCKED OUT
                window.destroy()                                                                                 #CLOSING THE LOGIN APPLICATION AFTER THE 'OK' HAS BEEN CLICKED ON THE MESSAGE BOX
                 
            elif trys > 0:                                                                                       #IF THE USER HAS MORE THAN 0 TRYS LEFT THEN THE FOLLOWING ACTIONS TAKE PLACE
                messagebox.showinfo("   ERROR!   ", """  Your username and/or password was incorrect!                                                        
                         You have """+str(trys)+str(" attempts left!") , icon="error")                           #DISPLAYING THE ERROR MESSAGE BOX WITH ATTEMPTS LEFT
                TRYS = TRYS+1                                                                                    #ADDS +1 TO THE 'TRYS' ARRAY TO KEEP COUNT
                trys = trys-1                                                                                    #TAKES -1 AWAY FROM THE 'trys' ARRAY TO DISPLAY REMAINDER OF ATTMEPTS 

def SignUpLoginWin():
    
    window.destroy() #CLOSING THE LOGIN APPLICATION
    SignUpApp()      #STARTING THE SIGN UP APPLICATION FOR THE USER TO SIGN UP IF THEY DO NOT HAVE AN ACCOUNT

window = Tk()                                 #DEFINING WHAT THE TKINTER WINDOW WILL BE DEFINED AS
logo = PhotoImage(file="CMPBANKINGLOGO.png")  #THIS IS THE PATH FOR THE IMAGE DISPLAYED WITHIN THE LOGIN WINDOW
Logo = Label (window, image=logo)             #CREATING THE LABEL THAT WILL DISPLAY THE CMP BANKING LOGO AT THE TOP OF THE LOGIN WINDOW
window.iconphoto(False, logo)                 #SETTING THE CMP LOGO IN THE TOP BAR OF THE WINDOW
window.resizable(0,0)                         #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable(width=FALSE, height=FALSE)   #THE USER CANNOT CHANGE THE SIZE OF THE LOGIN WINDOW
window.title ("CMP BANKING SYSTEM")           #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("500x600")                    #CONFIGURING THE FIXED SIZE OF THE LOGIN WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')          #CONFIGURING THE BACKGROUND OF THE LOGIN WINDOW TO BE WHITE

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
SignUp = Button (text="     SIGN UP     ", fg="red", command=SignUpLoginWin)                                                       #CREATING THE SIGN UP BUTTON 

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










#CMP9134M ADVANCED SOFTWARE ENGINEERING - CMP BANKING SYSTEM
#NATHAN JONES
#FEB/MAR 2023
