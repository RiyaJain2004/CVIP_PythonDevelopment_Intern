#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from datetime import date
from tkinter import messagebox as mb

root=Tk()
root.geometry("800x600")
root.title("Age Calculator")
root.config(bg ="#FFAEB9")  

pic=PhotoImage(file=r"C:\Users\riyaj\OneDrive\Pictures\Camera Roll\Age_Cal.png")
mypic=Label(image=pic)
mypic.pack(padx=15,pady=15)


now_date=str(date.today())
list_today=now_date.split("-")

def calculateAge():
    global today
    global mylabel
    user_date=int(dayEntry.get())
    user_month=int(monthEntry.get())
    user_year=int(yearEntry.get())

    enter_date= int(list_today[2])
    enter_month= int(list_today[1])
    enter_year= int(list_today[0])
    month=[31,28,31,30,31,30,31,31,30,31,30,31]

    if(user_date>enter_date):
        enter_month=enter_month-1
        enter_date=enter_date+month[user_month-1]

    if (user_month>enter_month):
        enter_year=enter_year-1
        enter_month=enter_month+12
    date_result=str(enter_date-user_date)
    month_result=str(enter_month-user_month)
    year_result=str(enter_year-user_year)

    mylabel=Label(root,text=f"{nameVal.get()} you are " +year_result+ " Years " +month_result+ " Months " +date_result+ " Days "+ " Old .",borderwidth=5,font=("Times New Roman",20,"bold"),bg='white',fg='black')
    mylabel.place(x=300,y=500)


def reset_entries():  

    nameEntry.delete(0, END) 
    yearEntry.delete(0, END)  
    monthEntry.delete(0, END)  
    dayEntry.delete(0, END)  
    mylabel.destroy()
    
    yearEntry.focus_set() 
    monthEntry.focus_set()  
    dayEntry.focus_set() 
    nameEntry.focus_set()
    
  
def reset():  

    reset_entries()  
    mb.showinfo("Reset Entries", "All Entries are reset successfully!")  


Label(text="Name",font=("Times New Roman",20,"bold"),background='green').place(x=200,y=250)
Label(text="Year",font=("Times New Roman",20,"bold"),background='yellow').place(x=200,y=300)
Label(text="Month",font=("Times New Roman",20,"bold"),background='red').place(x=200,y=350)
Label(text="Day",font=("Times New Roman",20,"bold"),background='light blue').place(x=200,y=400)

nameVal=StringVar()
yearVal=StringVar()
monthVal=StringVar()
dayVal=StringVar()

nameEntry=Entry(root,textvariable=nameVal,width=60,bd=3,font=("Times New Roman",20,"bold"))
nameEntry.place(x=300,y=250)

yearEntry=Entry(root,textvariable=yearVal,width=60,bd=3,font=("Times New Roman",20,"bold"))
yearEntry.place(x=300,y=300)

monthEntry=Entry(root,textvariable=monthVal,width=60,bd=3,font=("Times New Roman",20,"bold"))
monthEntry.place(x=300,y=350)

dayEntry=Entry(root,textvariable=dayVal,width=60,bd=3,font=("Times New Roman",20,"bold"))
dayEntry.place(x=300,y=400)

Button(text="Reset entries",font=20,bg='black',fg='white',width=25,height=2,command=reset).place(x=500,y=450)
Button(text='Calculate the Age',font=20,bg='black',fg='white',width=25,height=2,command=calculateAge).place(x=300,y=450)

root.mainloop()

