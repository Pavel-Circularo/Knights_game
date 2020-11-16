class Rytir():
    
    def __init__(self, u_cislo, o_cislo, vydrz, pozice_stitu, pozice_drevce):
        self.u_cislo = u_cislo
        self.o_cislo = o_cislo
        self.vydrz = vydrz
        self.pozice_stitu = pozice_stitu
        self.pozice_drevce = pozice_drevce

shield_pos = int(input("Kam dáme štít? (1-4): "))
drevec_pos = int(input("Kam dáme dřevec? (1-4): "))
        
rytir1 = Rytir(0, 0, 100, shield_pos, drevec_pos)
rytir2 = Rytir(0, 0, 100, shield_pos, drevec_pos)

typ_zbroje = int(input("Vyber si typ zbroje: 1 = zadna 2 = kozena 3 = krouzkova 4 = platova"))
def zbroj(rytir, typ_zbroje):
    if typ == 1:
        pass
    elif typ == 2:
        rytir.vydrz -= 3
        rytir.o_cislo += 1
    elif typ == 3:
        rytir.vydrz -= 5
        rytir.o_cislo += 3
    else:
        rytir.vydrz -= 7
        rytir.o_cislo += 4
        
rychlost_kone = int(input("Vyber si rychlost koně: 1 = cval 2 = klus 3 = trysk"))
def kun(rychlost_kone, rytir):
    if typ == 1:
        pass
    elif typ == 2:
        rytir.vydrz -= 3
        rytir.o_cislo += 1
    elif typ == 3:
        rytir.vydrz -= 5
        rytir.o_cislo += 3
    else:
        rytir.vydrz -= 7
        rytir.o_cislo += 4

