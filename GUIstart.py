import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


# noinspection SpellCheckingInspection
def okno():
    def pravidla():
        messagebox.showinfo("Pravidla",
                            """Cíl hry je sesadit rytíře ze sedla nebo mít na konci 3 kol více výdrže než on. Na začátku si vybereš vybevení, které určí tvé statistiky. 
Čím lepší vybavení, tím lepší obrana/útočné číslo ale větší ztráta výdrže. Např těžký dřevec přidá X k útočnému číslu, ale zase ubere Y výdrže za kolo. 
Poté si vybereš na jakou část těla chceš zaútočit drřevcem a kterou si budeš chránit štítem. Choose wisely!""")

    def hotovo():
        result = messagebox.askquestion("Opravdu?", "Jsi spokojen se svým výběrěm? Pokud jsi nezadal jméno budeš se jmenovat Kamil!")
        if result == "yes":
            seznam_vyberu[3] = jmeno.get()
            root.destroy()

    seznam_vyberu = ["kozena", "lehky", "klus", "Kamil"]

    def vyzbroj(arg):
        if arg == 1:
            messagebox.showinfo("Brnění", "Vybráno kožené brnění!")
            seznam_vyberu[0] = "kozena"
            lbl_brneni["text"] = "Kožená"
        elif arg == 2:
            messagebox.showinfo("Brnění", "Vybráno kroužkové brnění!")
            seznam_vyberu[0] = "krouzkova"
            lbl_brneni["text"] = "Kroužková"
        elif arg == 3:
            messagebox.showinfo("Brnění", "Vybráno plátěné brnění!")
            seznam_vyberu[0] = "platova"
            lbl_brneni["text"] = "Plátová"
        elif arg == 4:
            messagebox.showinfo("Dřevec", "Vybrán lehký dřevec!")
            seznam_vyberu[1] = "lehky"
            lbl_drevec["text"] = "Lehký"
        elif arg == 5:
            messagebox.showinfo("Dřevec", "Vybrán střední dřevec!")
            seznam_vyberu[1] = "stredni"
            lbl_drevec["text"] = "Střední"
        elif arg == 6:
            messagebox.showinfo("Dřevec", "Vybrán těžký dřevec!")
            seznam_vyberu[1] = "tezky"
            lbl_drevec["text"] = "Těžký"
        elif arg == 7:
            messagebox.showinfo("Kůň", "Vybrán klus!")
            seznam_vyberu[2] = "klus"
            lbl_kun["text"] = "Klus"
        elif arg == 8:
            messagebox.showinfo("Kůň", "Vybrán cval!")
            seznam_vyberu[2] = "cval"
            lbl_kun["text"] = "Cval"
        elif arg == 9:
            messagebox.showinfo("Kůň", "Vybrán trysk!")
            seznam_vyberu[2] = "trysk"
            lbl_kun["text"] = "Trysk"

    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('859x700')
    root.configure(background='#C1CDCD')
    root.title('Vítej!')

    # This is the section of code which creates the a label
    Label(root, text='Vítej v "Jouster"', bg='#C1CDCD', font=('courier', 20, 'bold')).place(x=293, y=10)
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
    Label(root, text='Tvůj výběr:', bg='#C1CDCD', font=('courier', 20, 'bold')).place(x=330, y=500)

    # This is the section of code which creates the label
    Label(root, text='Brnění:', bg='#C1CDCD', font=('courier', 10, 'bold')).place(x=350, y=540)
    lbl_brneni = Label(root, text="", bg='#C1CDCD')
    lbl_brneni.place(x=420, y=540)

    # This is the section of code which creates the label for offense number
    Label(root, text='Dřevec:', bg='#C1CDCD', font=('courier', 10, 'bold')).place(x=350, y=560)
    lbl_drevec = Label(root, text= "",bg='#C1CDCD')
    lbl_drevec.place(x=420, y=560)

    # This is the section of code which creates the label defense number
    Label(root, text='Rychlost koně:', bg='#C1CDCD', font=('courier', 10, 'bold')).place(x=294, y=580)
    lbl_kun = Label(root, text="", bg='#C1CDCD')
    lbl_kun.place(x=420, y=580)

    # This is the section of code which creates the label for text
    Label(root, text='Jak se jmenuje tvůj rytíř?', bg='#C1CDCD', font=('courier', 15, 'bold')).place(x=150, y=610)
    Button(root, text='Výběr hotov!', bg='#838B8B', font=('courier', 10, 'bold'), command=hotovo).place(x=360, y=650)

    """def vytiskni():
        seznam_vyberu[3] = jmeno.get()
        print(seznam_vyberu[3])"""
    #Button(root, text = "test", command = vytiskni).place(x=500, y=650)

    # This is the section of code which creates a text input box
    jmeno = StringVar()
    pepa = Entry(root, text = jmeno)
    pepa.place(x=500, y=615)

    root.mainloop()
    return seznam_vyberu
