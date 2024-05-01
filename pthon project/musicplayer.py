import pygame
import functools
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("Music Player")
music_player.geometry("600x550")
music_player.config(bg="#E1C9F8")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Roboto 10 bold ", bg="#E1C9F8", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def rewind():
    pygame.mixer.music.rewind()
def previous():
    current_index = play_list.curselection()[0]
    if current_index > 0:
        play_list.selection_clear(0, tkr.END)
        play_list.select_set(current_index - 1)
        play()
def next():
    current_index = play_list.curselection()[0]
    if current_index < len(song_list) - 1:
        play_list.selection_clear(0, tkr.END)
        play_list.select_set(current_index + 1)
        play()

Button1 = tkr.Button(music_player, width=5, height=3, font="Roboto 12 bold  ", text="PLAY", command=play, bg="#988DAE", fg="#40434a")
Button2 = tkr.Button(music_player, width=5, height=3, font="Roboto 12 bold  ", text="STOP", command=stop, bg="#E9C9F8", fg="#40434a")
Button3 = tkr.Button(music_player, width=5, height=3, font="Roboto 12 bold  ", text="rewind", command=rewind, bg="#C9D4F8", fg="#40434a")
Button4 = tkr.Button(music_player, width=5, height=3, font="Roboto 12 bold  ", text="previous", command=previous, bg="#A069D4", fg="#40434a")
Button5 = tkr.Button(music_player, width=5, height=3, font="Roboto 12 bold  ", text="next", command=next, bg="#7084B5", fg="#40434a")
var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Roboto 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
play_list.pack(fill="both", expand="yes")
music_player.mainloop()