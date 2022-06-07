# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:00:21 2021

@author: Kalyani

Greetings of the day, everybody!!
Here's my project titled: "Disaster Prediction on the basis of Rainfall"
under the guidance of: "ib@se Technologies"

"""

import tkinter as tk
import pandas as pd
from tkinter import messagebox
import prediction_disaster as pdis

top = tk.Tk()
top.config(bg = "skyblue")
top.geometry("800x450")

    
def new_window1():
    def pkeral():
        li = [[t1.get(), t2.get(), t3.get(), t4.get(), t5.get()]]
        d1 = pd.DataFrame(li, dtype = 'float')
        
        p = pdis.predictk(d1)
        if(p == 1):
            messagebox.showinfo("Prediction", "There are chances of flood")
        if(p == 0):
            messagebox.showinfo("Prediction", "There are no chances of flood")
        
        
    new1 = tk.Tk()
    new1.title("Keral's Flood Prediction")
    new1.geometry("700x500")
    new1.config(bg = "antique white")
    
    l1 = tk.Label(new1, text = "DISASTER PREDICTION SYSTEM", font = ["", 20], fg = "midnightblue", bg = "antique white")
    l2 = tk.Label(new1, text = " For Kerela ", font = ["verdana", 15], fg = "dodgerblue4", bg = "antique white")
    l1.place(x = 125, y = 75)
    l2.place(x = 270, y = 110)
    
    l = tk.Label(new1, text = "Please Enter the Rainfall Rate for Corresponding months", font = ["", 12], fg = "gray10", bg = "antique white")
    l.place(x = 100, y = 155)
    
    l = tk.Label(new1, text = "June", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 200)
    t1 = tk.Entry(new1, font = ["", 15])
    t1.place(x = 250, y = 200)
    
    l = tk.Label(new1, text = "July", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 240)
    t2 = tk.Entry(new1, font = ["", 15])
    t2.place(x = 250, y = 240)
    
    l = tk.Label(new1, text = "August", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 280)
    t3 = tk.Entry(new1, font = ["", 15])
    t3.place(x = 250, y = 280)
    
    l = tk.Label(new1, text = "October", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 320)
    t4 = tk.Entry(new1, font = ["", 15])
    t4.place(x = 250, y = 320)
    
    l = tk.Label(new1, text = "November", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 360)
    t5 = tk.Entry(new1, font = ["", 15])
    t5.place(x = 250, y = 360)
    
    b = tk.Button(new1, text = "Get Prediction", command = pkeral)
    b.place(x = 275, y = 400)
    
    
def new_window2():
    def pindia():
        li = [[tx1.get(), tx2.get(), tx3.get(), tx4.get()]]
        d1 = pd.DataFrame(li, dtype = 'float')
        print(d1)
        p = pdis.predictInd(d1)
        if(p == 1):
            messagebox.showinfo("Prediction", "There are chances of flood..")
        if(p == 0):
            messagebox.showinfo("Prediction", "There are no chances of flood..")
        
    new2 = tk.Tk()
    new2.title("India's Flood Prediction")
    new2.geometry("700x500")
    new2.config(bg = "antique white")
    l1 = tk.Label(new2, text = "DISASTER PREDICTION SYSTEM", font = ["", 20], fg = "midnightblue", bg = "antique white")
    l2 = tk.Label(new2, text = " For India ", font = ["verdana", 15], fg = "dodgerblue4", bg = "antique white")
    l1.place(x = 125, y = 75)
    l2.place(x = 270, y = 110)
        
    l = tk.Label(new2, text = "Please Enter the Rainfall Rate for Corresponding months", font = ["", 12], fg = "gray10", bg = "antique white")
    l.place(x = 100, y = 155)
        
    l = tk.Label(new2, text = "June", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 200)
    tx1 = tk.Entry(new2, font = ["", 15])
    tx1.place(x = 250, y = 200)
        
    l = tk.Label(new2, text = "July", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 240)
    tx2 = tk.Entry(new2, font = ["", 15])
    tx2.place(x = 250, y = 240)
        
    l = tk.Label(new2, text = "August", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 280)
    tx3 = tk.Entry(new2, font = ["", 15])
    tx3.place(x = 250, y = 280)

    l = tk.Label(new2, text = "September", font = ["", 15], bg = "antique white")
    l.place(x = 150, y = 320)
    tx4 = tk.Entry(new2, font = ["", 15])
    tx4.place(x = 250, y = 320)
        
    b = tk.Button(new2, text = "Get Prediction", command = pindia)
    b.place(x = 275, y = 370)
        
    

l1 = tk.Label(top, text = "DISASTER PREDICTION SYSTEM", font = ["", 24], fg = "midnightblue", bg = "skyblue")
l2 = tk.Label(top, text = "Based On Rainfall Analysis", font = ["verdana", 9], fg = "dodgerblue4", bg = "skyblue")
l1.place(x = 125, y = 100)
l2.place(x = 270, y = 135)

l3 = tk.Label(top, text = "--------------Please, Make a choice From Below--------------", font =["", 17], fg = "navy", bg = "skyblue")
l3.place(x = 100, y = 200)

b1 = tk.Button(top, text = "              Keral's              ", font = ["", 15], bg = "light cyan", command = new_window1)
b1.place(x = 250, y = 270)

b2 = tk.Button(top, text = "            All India's            ", font = ["", 15], bg = "light cyan", command = new_window2)
b2.place(x = 250, y = 325)

l4 = tk.Label(top, text = "ib@se Technologies - Python Machine Learning", font = ["", 8], fg = "black", bg = "skyblue")
l4.place(x = 260, y = 430)
top.mainloop()




































