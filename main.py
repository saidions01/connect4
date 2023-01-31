import tkinter as tk
from pygame import mixer
from tkinter import ttk

from Jeu import *


def main():

    game = Jeu()
        #Instantiate mixer
    mixer.init()
    #Load audio file
    mixer.music.load('backgroundSong.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()
    game.Jouer()
    


ws=tk.Tk()
ws.geometry("975x650")
ws.title("Puissance 4")

image=tk.PhotoImage(file="Web capture_21-1-2023_213937_www.canva.com.png")
phrase=tk.Label(ws,image=image,text="Bienvenu Dans Le Jeu Puissance 4",font=("Arial",60),pady=500)
phrase.pack()



bottom_frame=tk.Frame(ws)
start_btn = tk.Button(ws,text="Start",font=("Small fonts",19),bg="#f81d7f",fg="blue",width=8,command=lambda:main(),borderwidth=10)
start_btn.place(x=410,y=400) 
quit_btn=tk.Button(ws,text="Quit",font=("Small fonts",19),bg="#f81d7f",fg="blue",width=8,command=ws.destroy,borderwidth=10)
quit_btn.place(x=410,y=480) 

bottom_frame.pack(side=tk.BOTTOM,pady=10)

ws.mainloop()
