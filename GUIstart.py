import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


# noinspection SpellCheckingInspection
def okno():
    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = pepa.get()
        return userInput

    def pravidla():
        messagebox.showinfo("Pravidla",
                            """Cíl hry je sesadit rytíře ze sedla nebo mít na konci 3 kol více výdrže než on. Na začátku si vybereš vybevení, které určí tvé statistiky. 
Čím lepší vybavení, tím lepší obrana/útočné číslo ale větší ztráta výdrže. Např těžký dřevec přidá X k útočnému číslu, ale zase ubere Y výdrže za kolo. 
Poté si vybereš na jakou část těla chceš zaútočit drřevcem a kterou si budeš chránit štítem. Choose wisely!""")

    def hotovo():
        result = messagebox.askquestion("Opravdu?", "Jsi spokojen se svým výběrěm?")
        if result == "yes":
            root.destroy()

    #def nasadit():
     #   lbl["text"] = 5

    seznam_vyberu = ["kozena", "lehky", "klus", "kamil"]

    def vyzbroj(arg):
        vydrz = 0
        uc = 0
        uc2 = 0
        oc = 0
        if arg == 1:
            messagebox.showinfo("button 1", "Vybráno kožené brnění!")
            seznam_vyberu[0] = "kozena"
        elif arg == 2:
            messagebox.showinfo("button 2", "Vybráno kroužkové brnění!")
            seznam_vyberu[0] = "krouzkova"
        elif arg == 3:
            messagebox.showinfo("button 3", "Vybráno plátěné brnění!")
            seznam_vyberu[0] = "platova"
        elif arg == 4:
            messagebox.showinfo("button 4", "Vybrán lehký dřevec!")
            seznam_vyberu[1] = "lehky"
            uc += 5
            lbl["text"] = uc
        elif arg == 5:
            messagebox.showinfo("button 5", "Vybrán střední dřevec!")
            seznam_vyberu[1] = "stredni"
            uc += 10
            lbl["text"] = uc
        elif arg == 6:
            messagebox.showinfo("button 6", "Vybrán těžký dřevec!")
            seznam_vyberu[1] = "tezky"
            uc += 15
            lbl["text"] = uc
        elif arg == 7:
            messagebox.showinfo("button 7", "Vybrán klus!")
            seznam_vyberu[2] = "klus"
            uc2 += (uc + 2)
            lbl["text"] = uc2
        elif arg == 8:
            messagebox.showinfo("button 8", "Vybrán cval!")
            seznam_vyberu[2] = "cval"
            uc2 += (uc + 4)
            lbl["text"] = uc2
        elif arg == 9:
            messagebox.showinfo("button 9", "Vybrán trysk!")
            seznam_vyberu[2] = "trysk"
            uc2 += (uc + 6)
            lbl["text"] = uc2

    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('859x700')
    root.configure(background='#C1CDCD')
    root.title('Vítej!')

    # This is the section of code which creates the a label
    Label(root, text='Vítej v "Jou(k)ster"', bg='#C1CDCD', font=('courier', 20, 'bold')).place(x=293, y=10)
    # This is the section of code which creates the a label
    Label(root, text='Nejdřív si přecti', bg='#C1CDCD', font=('courier', 10, 'bold')).place(x=304, y=51)

    # This is the section of code which creates a button
    Button(root, text='Pravidla', bg='#838B8B', font=('courier', 10, 'bold'), command=pravidla).place(x=452, y=47)

    # This is the section of code which creates the a label
    Label(root, text='Vyber si brnění, dřevec a rychlost koně:', bg='#C1CDCD', font=('courier', 10, 'bold')).place(
        x=260, y=77)

    # This is the section of code which creates a button for leather armor
    leather = PhotoImage(master=root, file=r"C:\Users\pvesely\Coding\Knight_game\leather_armor.gif")
    Button(root, image=leather, command=lambda: vyzbroj(1)).place(x=197, y=110)

    # This is the section of code which creates a button for chainmail armor
    chainmail = PhotoImage(master=root, file=r"C:\Users\pvesely\Coding\Knight_game\chainmail_armor.gif")
    Button(root, image=chainmail, command=lambda: vyzbroj(2)).place(x=372, y=110)

    # This is the section of code which creates a button for plate armor 
    plate = PhotoImage(master=root, file=r"C:\Users\pvesely\Coding\Knight_game\plate_armor.gif")
    Button(root, image=plate, command=lambda: vyzbroj(3)).place(x=544, y=110)

    # This is the section of code which creates a button for lehky drevec
    lehky_drevec = PhotoImage(master=root, file=r"C:\Users\pvesely\Coding\Knight_game\lehky_drevec.gif")
    Button(root, image=lehky_drevec, command=lambda: vyzbroj(4)).place(x=245, y=250)

    # This is the section of code which creates a button for stredni:drevec
    stredni_drevec = PhotoImage(master=root, file=r"C:\Users\pvesely\Coding\Knight_game\stredni_drevec.gif")
    Button(root, image=stredni_drevec, command=lambda: vyzbroj(5)).place(x=410, y=250)

    # This is the section of code which creates a button for tezky drevec
    tezky_drevec = PhotoImage(master=root, file=r"C:\Users\pvesely\Coding\Knight_game\tezky_drevec.gif")
    Button(root, image=tezky_drevec, command=lambda: vyzbroj(6)).place(x=590, y=250)

    # This is the section of code which creates a button for klus
    Button(root, text='klus', bg='#838B8B', font=('courier', 10, 'bold'), command=lambda: vyzbroj(7)).place(x=238,y=430)

    # This is the section of code which creates a button for cval
    Button(root, text='cval', bg='#838B8B', font=('courier', 10, 'bold'), command=lambda: vyzbroj(8)).place(x=408,y=430)

    # This is the section of code which creates a button for trysk
    Button(root, text='trysk', bg='#838B8B', font=('courier', 10, 'bold'), command=lambda: vyzbroj(9)).place(x=580,y=430)

    # This is the section of code which creates the label
    Label(root, text='Tvoje statistiky:', bg='#C1CDCD', font=('courier', 20, 'bold')).place(x=293, y=500)

    vydrz = 100
    # This is the section of code which creates the label
    Label(root, text='Výdrž:', bg='#C1CDCD', font=('courier', 10, 'bold')).place(x=350, y=540)
    Label(root, text=vydrz).place(x=420, y=540)

    # This is the section of code which creates the label for offense number
    Label(root, text='Útočné číslo:', bg='#C1CDCD', font=('courier', 10, 'bold')).place(x=294, y=560)
    lbl = Label(root, text= 0)
    lbl.place(x=420, y=560)

    oc = 0
    # This is the section of code which creates the label defense number
    Label(root, text='Obranné číslo:', bg='#C1CDCD', font=('courier', 10, 'bold')).place(x=286, y=580)
    lbl2 = Label(root, text=oc)
    lbl2.place(x=420, y=580)

    # This is the section of code which creates the label for text
    Label(root, text='Jak se jmenuje tvůj rytíř?', bg='#C1CDCD', font=('courier', 15, 'bold')).place(x=150, y=610)
    Button(root, text='Výběr hotov!', bg='#838B8B', font=('courier', 10, 'bold'), command=hotovo).place(x=360, y=650)

    def vytiskni():
        seznam_vyberu[3] = jmeno.get()
        print(seznam_vyberu[3])
    Button(root, text = "test", command = vytiskni).place(x=500, y=650)
    # This is the section of code which creates a text input box
    jmeno = StringVar()
    pepa = Entry(root, text = jmeno)
    pepa.place(x=500, y=615)

    root.mainloop()
    return seznam_vyberu
