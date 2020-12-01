import random as rd

class Rytir():
    def __init__(self,jmeno,uc,oc,s,pos_d,pos_s,unava):
        self.jmeno = jmeno
        self.uc = uc
        self.oc = oc
        self.s = s
        self.pos_d = pos_d
        self.pos_s = pos_s
        self.unava = unava
        
    def priprava_pozic(self):
        # Vyber pozice drevce        
        while True:
            pozice_drevce = (input("Kam miris drevcem H,L,P,T:")).lower()
            if pozice_drevce not in "h,l,p,t":
                print("Spatne zadana pozice drevce")
                continue
            else:
                self.pos_d = pozice_drevce
                break
        # Vyber pozice stitu        
        while True:
            pozice_stitu = (input("Pozice stitu H,L,P,T:")).lower()
            if pozice_stitu not in "h,l,p,t":
                print("Spatne zadana pozice stitu")
                continue
            else:
                self.pos_s = pozice_stitu
                break

       
    def utok(self,kostka_uc,rychlost_uc,utok_unava):
        # Vypocet utocneho cisla
        self.uc = rd.randrange(1,kostka_uc + 1) + rychlost_uc
        # Vypocet unavy
        self.s = self.s + self.unava + utok_unava

    def obrana(self):
        # Vypocet obrany
        self.oc = self.oc + rd.randrange(0,7)
        
def vytvor_rytire():
    jmeno = input("Jmeno: ")
    s = 100
    uc = 0
    oc = 0
    pos_d =""
    pos_s = ""
    typ_zbroje = {"zadna":[0,0], "kozena":[-3,1], "krouzkova":[-5,3],"platova":[-7,4]}
    
    while True:
        zbroj = (input("Zadej druh zbroje - zadna,kozena,krouzkova,platova: ")).lower()
        if zbroj not in typ_zbroje.keys():
            print("Špatne zadana zbroj")
            continue
        else:
            unava = typ_zbroje[zbroj][0]
            oc = oc + typ_zbroje[zbroj][1]
            break
    
    return Rytir(jmeno,uc,oc,s,pos_d,pos_s,unava)

def priprava_utoku():
    # Parametry vybavení
    uc_unava = 0
    rychlost_unava = 0
    typ_drevce = {"lehky":[-5,4],"stredni":[-10,6],"tezky":[-15,10]}
    kun = {"cval":[0,0],"klus":[-3,2],"trysk":[-5,3]}
    # Vyber drevce
    while True:
        drevec = (input ("Zvol si drevec lehky/stredni/tezky: ")).lower()
        if drevec not in typ_drevce.keys():
            print("Spatne zadany drevec")
            continue
        else:
            kostka_uc = typ_drevce [drevec] [1]
            uc_unava = uc_unava + typ_drevce [drevec] [0]
            break
    # Vyber ryhlosti       
    while True:
        rychlost = (input("Zadej rychlost kone cval/klus/trysk: ")).lower()
        if rychlost not in kun.keys():
            print("Spatne zadana rychlost")
            continue
        else:
            rychlost_uc = kun [rychlost] [1]
            rychlost_unava =  rychlost_unava + kun [rychlost] [0]
            break
    utok_unava = rychlost_unava + uc_unava
        
    return kostka_uc , rychlost_uc , utok_unava
    
  
def stret(R1,R2):
    global R1_blok,R2_blok
    if R1.pos_s == R2.pos_d:
        R1_blok = 1
        
    if R2.pos_s == R1.pos_d:
        R2_blok = 1
        
    # Zasah R1    
    if R1.uc > R2.oc and R2_blok == 0: 
         R2.s = R2.s - R1.uc
         
    # Zasah R2    
    if R2.uc > R1.oc and R1_blok == 0:
        R1.s = R1.s - R2.uc
        
    if ((R1.uc  <= R2.oc) and (R2.uc <= R1.uc)) or (R1_blok == 1 and R2_blok == 1):
        pass
        
# Kontrola shození před koncem turnaje        
def shozeni(R1,R2):
    if R1.s <= 0 and R2.s > 0:
        return True
    
    elif R2.s <= 0 and R1.s > 0:
        return True
        
    elif R2.s <= 0 and R1.s <= 0:
        return True

def komentator(R1,R2):
    # Vyhlaseni viteze
    if konec == True:
        if R1.s > R2.s and R1.s > 0:
            print(f"Zvítězil rytíř {R1.jmeno}")
            
        elif R2.s > R1.s and R2.s > 0:
            print(f"Zvítězil rytíř {R2.jmeno}")
    
        elif R1.s == R2.s or (R1.s and R2.s) <= 0:
            print("Remíza")
    else:
        # Prubeh turnaje
        if R1.pos_s == R2.pos_d:
            print(f"Rytíř {R1.jmeno} odrazil útok štítem")
        if R2.pos_s == R1.pos_d:
            print(f"Rytíř {R2.jmeno} odrazil útok štítem")
        if R1.uc > R2.oc and R2_blok == 0: 
             print(f"Rytíř {R1.jmeno} překonal silou: {R1.uc}, obranu soupeře {R2.oc}.")
        if R2.uc > R1.oc and R1_blok == 0:
            print(f"Rytíř {R2.jmeno} překonal silou: {R2.uc}, obranu soupeře: {R1.oc}.")
        if ((R1.uc  <= R2.oc) and (R2.uc <= R1.uc)) or (R1_blok == 1 and R2_blok == 1):
            print("Rytíři se ubránili soupeři")
         
        if shozeni(R1,R2) == True:
            if R1.s <= 0 and R2.s > 0:
                print(f"Rytíř {R1.jmeno} je shozen ze sedla v {p}. kole")
            
            elif R2.s <= 0 and R1.s > 0:
                print(f"Rytíř {R2.jmeno} je shozen ze sedla v {p}. kole")
                
            elif R2.s <= 0 and R1.s <= 0:
                print(f"Oba rytíři jsou shozeni ze sedla v {p}. kole")
                
        if R1.s > 0 and R2.s > 0 and p < pocet_kol: 
            print(f"Rytíř {R1.jmeno} nastupuje do {p+1}. kola s výdrží: {R1.s}")
            print(f"Rytíř {R2.jmeno} nastupuje do {p+1}. kola s výdrží: {R2.s}")       
        
    
# Hlavní program   
def turnaj():
    global p, pocet_kol, konec, R1_blok, R2_blok
    p = 0
    konec = False
    pocet_kol = 3
    
    R1 = vytvor_rytire()
    R2 = vytvor_rytire()
    
   
    while p < pocet_kol:
        p += 1

        print(20*"-" + f" KOLO {p} " + 20*"-")
        R1_blok = 0
        R2_blok = 0
        
        # Nastaveni utoku a obrany R1
        parametry_utoku  = priprava_utoku()
        R1.utok(parametry_utoku[0] , parametry_utoku[1] , parametry_utoku [2])
        R1.priprava_pozic()
        R1.obrana()
        
        # Nastaveni utoku a obrany R2
        parametry_utoku  = priprava_utoku()
        R2.utok(parametry_utoku[0] , parametry_utoku[1] , parametry_utoku [2])
        R2.priprava_pozic()
        R2.obrana()

        stret(R1,R2)
        
        if shozeni(R1,R2):
            komentator(R1, R2, stav = "shozeni")
            break
        komentator(R1, R2, stav = "probiha")
        
    komentator(R1, R2, stav = "konec")
    
### Testovani
def vitez(R1,R2):
    global a,b,c
    if R1.s > R2.s and R1.s > 0:
        a = a + 1
        
    elif R2.s > R1.s and R2.s > 0:
        b = b + 1

    elif R1.s == R2.s or (R1.s and R2.s) <= 0:
        c = c + 1
        
def automaticky_turnaj():
    global p, pocet_kol, konec, R1_blok, R2_blok,a,b,c,d,e,f
    p = 0
    konec = False
    pocet_kol = 3
    
    # Ri (Jmeno, + utocne cislo,  + obranne cislo,  + vydrz, pozice drevce, pozice stitu,  - unava_zbroj)
    
    with open ("Rt.csv", mode = "a", encoding = "utf-8") as data:
        # Vytvoreni R1
        unava_nahodna = rd.randint(0,25)
        zbroj_nahodna = rd.randint(0,25)
        R1 = Rytir("Alistar",0,zbroj_nahodna,50,"l","h",unava_nahodna)
        print("Nahodna zbroj",zbroj_nahodna,"Nahodna unava",unava_nahodna, file = data)
        
        # Vytvoreni R2
        unava_nahodna = rd.randint(0,25)
        zbroj_nahodna = rd.randint(0,25)
        R2 = Rytir("Duncan",0,zbroj_nahodna,50,"r","t",0)
        print("Nahodna zbroj",zbroj_nahodna,"Nahodna unava",unava_nahodna, file = data)
    
        #while p < pocet_kol:
            p += 1
            
            # R1_blok = 0
            # R2_blok = 0
            
            # # Ri(+ kostka utoku, + rychlost, -unava)
            
            # # Nastavni parametru R1
            # kostka_nahodna = rd.randint(1,25)
            # rychlost_nahodna = rd.randint(1,25)
            # vydrz_nahodna = rd.randint(-25,0)
            
            # R1.utok(kostka_nahodna,rychlost_nahodna,vydrz_nahodna)
            # print ("R1: ","Kostka",kostka_nahodna,"Rychlost",rychlost_nahodna,"Vydrz", vydrz_nahodna, file = data )
            
            # # Nastaveni parametru R2
            # kostka_nahodna = rd.randint(1,25)
            # rychlost_nahodna = rd.randint(1,25)
            # vydrz_nahodna = rd.randint(-25,0)
            # R2.utok(kostka_nahodna,rychlost_nahodna,vydrz_nahodna)
            # print ("R2: ","Kostka",kostka_nahodna,"Rychlost",rychlost_nahodna,"Vydrz", vydrz_nahodna, file = data )
            
            # R1.obrana()
            # print("R1 obrana: ",R1.oc, file  = data)
            # R2.obrana()
            # print("R2 obrana: ",R2.oc, file = data)
            
        a = generator()    
        # a =  [[],[],[],......]
             
        for data_R1 in a:
            for data_R2 in a:
                R1 = vytvor rytire(data_R1)
                R2 = vytvor_rytire(data_R2)
                for i in range(3):
                    stret(R1,R2)
                    
                data_turnaj = vitez(R1,R2)
                statistika(data_R1,data_R2,data_turnaj)
                    # if R1.s <= 0 and R2.s > 0:
                    #     d = d + 1
                    #     continue
                
                    # elif R2.s <= 0 and R1.s > 0:
                    #     e = e + 1
                    #     continue
                        
                    # elif R2.s <= 0 and R1.s <= 0:
                    #     f = f + 1
                    #     continue
                


# def test():
#     global a,b,c,d,e,f 
#     pocet_spusteni = 1
    
#     a = 0 # Vyhra R1
#     b = 0 # Vyhra R2
#     c = 0 # Remiza
#     d = 0 # Počet shození R1
#     e = 0 # Počet shození R2
#     f = 0 # Počet shození oba

#     for i in range (0,pocet_spusteni):
#         automaticky_turnaj()

test()

    



def generator():
    data_R = [0,0,50,0]

    
    
    return()


def statistika(R1,R2):
     open.....:
         # ";".join(slouceny_seznam)
