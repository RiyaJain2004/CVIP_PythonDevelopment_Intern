#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image


def match_char_remove(list1,list2):
    for i in range(len(list1)):
        for j in range (len(list2)):

            if list1[i] == list2[j]:
                c=list1[i]
                list1.remove(c)
                list2.remove(c)

                list3=list1+["*"]+list2
                return[list3,True]
            
    list3=list1+["*"]+list2
    return[list3,False]

def say_st():
    p1=player1.get()
    p1=p1.lower()
    p1.replace(" ", " ")
    p1_list=list(p1)


    p2=player2.get()
    p2=p2.lower()
    p2.replace(" ", " ")
    p2_list=list(p2)


    pro = True
    while pro:
        ret_list = match_char_remove(p1_list,p2_list)
        con_list = ret_list[0]
        pro = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index +1 : ]
    count = len(p1_list)+len(p2_list)

    result = ["Friends" , "Love" , "Affection" , "Marriage" , "Enemy" , "Siblings"]

    while len(result)>1:
        split_index=(count%len(result)-1)

        if split_index>=0:
            right=result[split_index+1:]
            left=result[:split_index]
            result=right+left
        else:
            result=result[:len(result)-1]
    st.insert(10,result[0])

def reset_entries():
    player1.delete(0,END)
    player2.delete(0,END)
    st.delete(0,END)

    player1.focus_set() 
    player2.focus_set()
    st.focus_set()
    
def reset():  
    reset_entries()  
    mb.showinfo("Reset Entries", "All Entries are reset successfully!") 

if __name__ == "__main__":
    root=Tk()
    root.title("Flame Game")
    root.config(bg ="light blue")  
    
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()

    root.geometry("%dx%d" % (width, height))
    root.resizable(False, False)


    canvas1 = Canvas (root, width = width, height = height)
    canvas1.pack(fill = "both", expand = True)


    bg = PhotoImage(file = "C:\\Users\\riyaj\\OneDrive\\Pictures\\Camera Roll\\background1.png", master = root)

    canvas1.create_image(0, 0, image = bg, anchor = "nw")
    
    
    label=tk.Label(root, text="Flames Game",font=("Times New Roman",30,"bold"),bg='yellow',fg='black',width=15,height=2,borderwidth=2,relief="solid")
    label.place(x=450,y=100)
    label1=Label(root, text="Name 1",font=("Times New Roman",20,"bold"),width=8,background='green',borderwidth=2,relief="sunken")
    label1.place(x=200,y=250)
    label2=Label(root, text="Name 2",font=("Times New Roman",20,"bold"),width=8,background='yellow',borderwidth=2,relief="sunken")
    label2.place(x=200,y=300)
    label3=Label(root, text="Status",font=("Times New Roman",20,"bold"),width=8,background='pink',borderwidth=2,relief="sunken")
    label3.place(x=200,y=350)

    player1 = Entry(root, width=60,font=("Times New Roman",20,"bold"),borderwidth=2,relief="ridge")
    player1.place(x=350,y=250)
    player2 = Entry(root,width=60, font=("Times New Roman",20,"bold"),borderwidth=2,relief="ridge")
    player2.place(x=350,y=300)
    st = Entry(root,width=60,font=("Times New Roman",20,"bold"),borderwidth=2,relief="ridge")
    st.place(x=350,y=350)


    button1 = Button(root, text= "Relation Status",font=20,bg='black',fg='white',width=25,height=2,command=say_st,borderwidth=2,relief="raised")
    button2 = Button(root, text="Reset entries",font=20,bg='black',fg='white',width=25,height=2,command=reset,borderwidth=2,relief="raised")
  

    button1_canvas = canvas1.create_window( 300, 450, anchor = "nw", window = button1)
  
    button2_canvas = canvas1.create_window( 600, 450, anchor = "nw", window = button2)
   
    

root.mainloop()
    

