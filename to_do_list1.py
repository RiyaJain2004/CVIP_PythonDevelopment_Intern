#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter
from tkinter import *
import tkinter.messagebox as mb
import pickle

root=tkinter.Tk()
root.title("To-Do-List")
root.config(bg ="white")
root.geometry("800x600")

def add_task():
    task = entry_task.get()
    if task !="":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message= "You must enter a task.")

def delete_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title='Warning!', message="You must select a task.")

def load_task():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0,tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat .")
    

def save_task():
    tasks= listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks,open("tasks.dat","wb"))

def reset_entries():
    listbox_tasks.delete(0,END)
    listbox_tasks.focus_set()
    

def reset():  
    reset_entries()  
    mb.showinfo("Reset Entries", "All Entries are reset successfully!")  


frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks=tkinter.Listbox(frame_tasks, font=("Times New Roman",16,"bold"),height=18, width= 150)
listbox_tasks.pack(side=tkinter.LEFT)
listbox_tasks.config(bg ="light blue")

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill= tkinter.Y)

listbox_tasks.config(yscrollcommand= scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task=tkinter.Entry(root, font=("Times New Roman",18,"bold"),width= 150)
entry_task.pack()

button_add_tasks=tkinter.Button(root,text="Add Task", font=("Times New Roman",18,"bold"),background='green',height=1,width=150, command=add_task)
button_add_tasks.pack()

button_delete_tasks=tkinter.Button(root,text="Delete Task",font=("Times New Roman",18,"bold"),background='yellow',height=1,width=150, command=delete_task)
button_delete_tasks.pack()

button_load_task=tkinter.Button(root,text="Load Task", font=("Times New Roman",18,"bold"),background='red',height=1,width=150, command=load_task)
button_load_task.pack()

button_save_tasks=tkinter.Button(root,text="Save Task",font=("Times New Roman",18,"bold"),background='pink',height=1,width=150, command=save_task)
button_save_tasks.pack()

button_reset_tasks=tkinter.Button(root,text="Reset Task",font=("Times New Roman",18,"bold"),background='light green',height=1,width=150, command=reset)
button_reset_tasks.pack()

root.mainloop()

