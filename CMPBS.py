#CMP9134M ADVANCED SOFTWARE ENGINEERING - CMP BANKING SYSTEM
#NATHAN JONES
#FEB 2023

from tkinter import ttk                                          #IMPORTING THE TKK MODULE THAT ALLOWS FOR TABBED WIDGETS
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry  #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  #ALLOWING FOR THE MATPLOTLIB GRAPHS TO BE INSERTED INTO THE TKINTER GUI'S
from PIL import Image, ImageTk                                   #ALLOWS FOR THE IMPORTS OF IMAGES INTO THE PROGGRAM TO MAKE IT VISUALLY LOOK MORE PROFESSIONAL

import tkinter as tk                                             #IMPORTING THE TKINTER MODULE TO BE USED IN THE PROGRAM
import sys                                                       #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON
import os.path                                                   #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS
import os                                                        #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import matplotlib.pyplot as plt                                  #IMPORTING MATPLOTLIB SO THAT GRAPHS CAN BE CREATED AND PRODUCED IN THE PROGRAM
import pandas as pd                                              #ALLOWS FOR CERTIAN MATHMATICAL FUNCTIONS AND READING OF CSV DATA TO TAKE PLACE

def MainMenu():
    
    Menu = Tk()
    Menu.title("CMP Banking System")
    Menu.resizable(width=FALSE, height=FALSE)
    Menu.geometry("1400x700")
    tabControl = ttk.Notebook(Menu)

    style = ttk.Style()
    style.configure("W.TFrame", foreground="white", background="white")

    WelcomeTab = ttk.Frame(style="W.TFrame")

    for line in open("temp.txt","r").readlines():                #READING EACH LINE WITHIN THE 'temp' FILE
        data = line.split()
        name = data[0]
    
    S1 = Label(WelcomeTab, text=" ", background="white")                                                      #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
    Title = Label(WelcomeTab, text="CMP BANKING SYSTEM", font='Helvetica 12 bold', bg="white")                                              #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    S2 = Label(WelcomeTab, text=" ", background="white")                                                      #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
    SubTitle = Label(WelcomeTab, text="Welcome To The CMP Banking System!", font='Helvetica 10 bold', bg="white")                                                                #CREATING A SUB HEADING FOR THE DESCRIPTION 
    S3 = Label(WelcomeTab, text=" ", background="white")                                                      #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE BETWEEN 
    
    WelcomeMsg = Label(WelcomeTab, text="Welcome " +str(name), font='Helvetica 10', bg="white")
    
    S1.pack()
    Title.pack()
    S2.pack()
    SubTitle.pack()
    S3.pack()
    WelcomeMsg.pack()
    
    def BalenceSheet():

        BalenceTab = ttk.Frame(style="W.TFrame")
        

    
    tabControl.add(WelcomeTab, text='Welcome Page')
    tabControl.add(BalenceTab, text='Balence Sheet')
    tabControl.pack(expand = 1, fill ="both")
    
MainMenu()
#CMP9134M ADVANCED SOFTWARE ENGINEERING - CMP BANKING SYSTEM
#NATHAN JONES
#FEB 2023
