
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time

def postava():
    window = tk.Tk()
    window.geometry("800x700")
    window.title("Úder/Obrana")

    label = Label(window, text = "Vyber místo úderu dřevcem/ochrany štítem", font = (None, 30))
    label.pack(side = TOP)
    frame = Frame(window)
    frame.pack()
    bottomframe = Frame(window)
    bottomframe.pack(side = BOTTOM)

    o_hlava = PhotoImage(master=frame, file= r"C:\Users\pvesely\Coding\Knight_game\hlava.gif")
    o_torso = PhotoImage(master=bottomframe, file= r"C:\Users\pvesely\Coding\Knight_game\torso.gif")
    o_leva_ruka = PhotoImage(master=bottomframe, file= r"C:\Users\pvesely\Coding\Knight_game\leva_ruka.gif")
    o_prava_ruka = PhotoImage(master=bottomframe, file= r"C:\Users\pvesely\Coding\Knight_game\prava_ruka.gif")

    miridlo = ["H"]

    def h_vyber():
        result = messagebox.askquestion("Select", "Chceš vybrat hlavu?",)
        if result == "yes":
            window.destroy()
    def lr_vyber():
        result = messagebox.askquestion("Select", "Chceš vybrat levou ruku?",)
        if result == "yes":
            window.destroy()
            miridlo[0] = "L"
    def pr_vyber():
        result = messagebox.askquestion("Select", "Chceš vybrat pravou ruku?",)
        if result == "yes":
            window.destroy()
            miridlo[0] = "P"
    def t_vyber():
        result = messagebox.askquestion("Select", "Chceš vybrat torso?",)
        if result == "yes":
            window.destroy()
            miridlo[0] = "T"

    hlava = tk.Button(master= frame, image = o_hlava, cursor= "X_cursor", command = h_vyber)
    hlava.grid(row= 0, column = 1, sticky = "s")

    leva_ruka = tk.Button(master= bottomframe,  image = o_leva_ruka, cursor= "X_cursor", command = lr_vyber)
    leva_ruka.grid(row=1, column=0, sticky="n")

    prava_ruka = tk.Button(master= bottomframe, image = o_prava_ruka, cursor= "X_cursor", command = pr_vyber)
    prava_ruka.grid(row=1, column=2, sticky="n")

    torso = tk.Button(master= bottomframe, image = o_torso, cursor= "X_cursor", command = t_vyber)
    torso.grid(row=1, column=1, sticky="nsew")

    window.mainloop()
    return miridlo[0]
