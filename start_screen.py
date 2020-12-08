import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


def start():

    def single():
        result = messagebox.askquestion("Single", "Chceš hrát singleplayer?")
        if result == "yes":
            sp[0] = True
            root.destroy()

    def multi():
        result = messagebox.askquestion("Multi", "Chceš hrát multiplayer?")
        if result == "yes":
            sp[0] = False
            root.destroy()

    root = Tk()
    root.geometry('960x540')
    wallp = PhotoImage(master=root, file=r"C:\Users\pvesely\Coding\Knight_game\start_screen.gif")

    root.configure(bg="white")
    root.title('Start')

    sp = [True]

    Label(root,image = wallp).place(x=0, y=0)
    Label(root,text = "JOUSTER", bg='#e6d9c0', font=('courier', 30, 'bold')).place(x=150, y=40)

    singlebutt = Button(root, text='Singleplayer', bg='#838B8B', font=('courier', 10, 'bold'), command=single)
    singlebutt.place(x=120, y=100)
    multibutt = Button(root, text='Multiplayer', bg='#838B8B', font=('courier', 10, 'bold'), command=multi)
    multibutt.place(x=240, y=100)

    root.mainloop()
    return sp[0]
