#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer        
import os

mixer.init()


def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")


def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")



if __name__ == "__main__":
    root=Tk()
    root.title("Music Player Application")
    root.config(bg ="light blue")  
    
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()


    root.geometry("%dx%d" % (width, height))
    root.resizable(False, False)


    canvas1 = Canvas (root, width = width, height = height)
    canvas1.pack(fill = "both", expand = True)

    bg = PhotoImage(file = "C:\\Users\\riyaj\\OneDrive\\Pictures\\Camera Roll\\music_img1.png", master = root)

    canvas1.create_image(0, 0, image = bg, anchor = "nw")

    

    listbox_frame = LabelFrame(root, text='Playlist', font=('Times new roman', 18,'bold'),bg='red')
    listbox_frame.place(x=800, y=100, height=500, width=500)


    current_song = StringVar(root, value='<Not selected>')
    
    song_status = StringVar(root, value='<Not Available>')
    

    playlist = Listbox(listbox_frame, font=('Times new roman', 11,'bold'), selectbackground='silver',height=500)


    scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
    scroll_bar.pack(side=RIGHT, fill=BOTH)

    playlist.config(yscrollcommand=scroll_bar.set)

    scroll_bar.config(command=playlist.yview)

    playlist.pack(fill=BOTH, padx=5, pady=5)
 

    label=tk.Label(root, text="MUSICAL BLISS !!",font=("Times New Roman",25,"bold"),bg='yellow',fg='black',width=15,height=2,borderwidth=2,relief="groove")
    label.place(x=250,y=100)
    
    label1=Label(root, text="Currently playing",font=("Times New Roman",20,"bold"),width=16,height=1,background='green',borderwidth=3,relief="sunken")
    label1.place(x=100,y=250)

    
    song_lbl = Label(root, textvariable=current_song, bg='pink', font=("Times new roman", 13,"bold"), width=35,height=2,borderwidth=3,relief="sunken")
    song_lbl.place(x=400, y=250)

    pause_btn = Button(root, text='Pause', bg='yellow',fg='black', font=("Times new roman", 18,"bold"), width=6,height=2,command=lambda: pause_song(song_status),borderwidth=3,relief="raised")
    stop_btn = Button(root, text='Stop', bg='red',fg='black', font=("Times new roman", 18,"bold"), width=6,height=2,command=lambda: stop_song(song_status),borderwidth=3,relief="raised")
    play_btn = Button(root, text='Play', bg='pink', fg='black',font=("Times new roman", 18,"bold"), width=6,height=2,command=lambda: play_song(current_song, playlist, song_status),borderwidth=3,relief="raised")
    resume_btn = Button(root, text='Resume', bg='green',fg='black', font=("Times new roman", 18,"bold"), width=6,height=2,command=lambda: resume_song(song_status),borderwidth=3,relief="raised")


    pause_btn_canvas = canvas1.create_window( 100, 450, anchor = "nw", window = pause_btn)
    stop_btn_canvas = canvas1.create_window( 250, 450, anchor = "nw", window = stop_btn)
    play_btn_canvas = canvas1.create_window( 400, 450, anchor = "nw", window = play_btn)
    resume_btn_canvas = canvas1.create_window( 550, 450, anchor = "nw", window = resume_btn)


    load_btn = Button(root, text='Load Directory -->', bg='grey', font=("Times new roman", 18,"bold"), width=45, command=lambda: load(playlist),borderwidth=3,relief="sunken")
    load_btn_canvas = canvas1.create_window( 100, 550, anchor = "nw", window = load_btn)
    

    tlabel=Label(root, textvariable=song_status, bg='Blue', font=('Times new roman', 15,"bold"), width=115,justify=LEFT)
    tlabel.place(x=0, y=700)

root.update()
root.mainloop()
    

