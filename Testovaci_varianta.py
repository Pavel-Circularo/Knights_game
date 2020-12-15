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
        
class Figurant (Rytir):
    
    def utok(self,kostka_uc,rychlost_uc,utok_unava):
        # Vypocet utocneho cisla
        self.uc = round(kostka_uc/2) +1 + rychlost_uc
        # Vypocet unavy
        self.s = self.s + self.unava + utok_unava

    def obrana(self):
        # Vypocet obrany
        self.oc = self.oc + 4
    
def vytvor_rytire(typ_hrace):
    s = 40
    uc = 0
    oc = 0
    pos_d =""
    pos_s = ""
    typ_zbroje = {"zadna":[0,0], "kozena":[-1,5], "krouzkova":[-2,8],"platova":[-3,11]}
    
    if typ_hrace == "hrac":
        jmeno = input("Jmeno: ")
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
    
    elif typ_hrace == "pocitac":
        jmeno = "Rytir"
        zbroj = rd.choice(("zadna","kozena","krouzkova","platova"))
        unava = typ_zbroje[zbroj][0]
        oc = oc + typ_zbroje[zbroj][1]
    
        return Rytir(jmeno,uc,oc,s,pos_d,pos_s,unava)

def priprava_utoku(typ_hrace):
    # Parametry vybavení
    uc_unava = 0
    rychlost_unava = 0
    typ_drevce = {"lehky":[0,5],"stredni":[-1,8],"tezky":[-2,15]}
    kun = {"cval":[0,0],"klus":[-1,3],"trysk":[-3,7]}
    
    if typ_hrace == "hrac":
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
    
    elif typ_hrace == "pocitac":
            drevec = rd.choice(("lehky","stredni","tezky"))
            kostka_uc = typ_drevce [drevec] [1]
            uc_unava = uc_unava + typ_drevce [drevec] [0]
            # Vyber ryhlosti       
            rychlost = rd.choice(("cval","klus","trysk"))
            rychlost_uc = kun [rychlost] [1]
            rychlost_unava =  rychlost_unava + kun [rychlost] [0]
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

def komentator(R1,R2,stav):
    # Vyhlaseni viteze
    if stav == "konec":
        if R1.s > R2.s and R1.s > 0:
            print(f"Zvítězil rytíř {R1.jmeno}")
            
        elif R2.s > R1.s and R2.s > 0:
            print(f"Zvítězil rytíř {R2.jmeno}")
    
        elif R1.s == R2.s or (R1.s and R2.s) <= 0:
            print("Remíza")
            
    elif stav == "probiha":
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
        if p < 3:
            print(f"Rytíř {R1.jmeno} nastupuje do {p+1}. kola s výdrží: {R1.s}")
            print(f"Rytíř {R2.jmeno} nastupuje do {p+1}. kola s výdrží: {R2.s}") 
         
    elif stav == "shozen":
        if R1.s <= 0 and R2.s > 0:
            print(f"Rytíř {R1.jmeno} je shozen ze sedla v {p}. kole")
        
        elif R2.s <= 0 and R1.s > 0:
            print(f"Rytíř {R2.jmeno} je shozen ze sedla v {p}. kole")
            
        elif R2.s <= 0 and R1.s <= 0:
            print(f"Oba rytíři jsou shozeni ze sedla v {p}. kole")
            
def easter_egg(R1,R2):
    if R1.jmeno.lower() == "mintaka" or R2.jmeno.lower() == "mintaka":
        return True
                    
# Multiplayer
def turnaj_MP():
    global p, pocet_kol,R1_blok, R2_blok
    p = 0
    pocet_kol = 3
    
    R1 = vytvor_rytire(typ_hrace = "hrac")
    R2 = vytvor_rytire(typ_hrace = "hrac")
   
    if easter_egg(R1,R2) == True:
        print ("Soupeř se vzdal.")
        return
            
    while p < pocet_kol:
        p += 1

        print(20*"-" + f" KOLO {p} " + 20*"-")
        R1_blok = 0
        R2_blok = 0
        
        # Nastaveni utoku a obrany R1
        parametry_utoku  = priprava_utoku(typ_hrace = "hrac")
        R1.utok(parametry_utoku[0] , parametry_utoku[1] , parametry_utoku [2])
        R1.priprava_pozic()
        R1.obrana()
        
        # Nastaveni utoku a obrany R2
        parametry_utoku  = priprava_utoku(typ_hrace = "hrac")
        R2.utok(parametry_utoku[0] , parametry_utoku[1] , parametry_utoku [2])
        R2.priprava_pozic()
        R2.obrana()

        stret(R1,R2)
        
        if shozeni(R1,R2) == True:
            komentator(R1,R2,stav = "shozen")
            break
        komentator(R1, R2, stav = "probiha")
        
    komentator(R1,R2, stav = "konec")
    
# Singleplayer
def turnaj_SP():
    global p, pocet_kol,R1_blok, R2_blok
    p = 0
    pocet_kol = 3
    
    # Tvorba rytire uzivatelem
    R1 = vytvor_rytire(typ_hrace = "hrac")
    parametry_utoku  = priprava_utoku(typ_hrace = "hrac")
    R1.utok(parametry_utoku[0] , parametry_utoku[1] , parametry_utoku [2])
    
    # Automaticky vytvoreny rytir
    R2 = vytvor_rytire(typ_hrace = "pocitac")
    parametry_utoku  = priprava_utoku(typ_hrace = "pocitac")
    R2.utok(parametry_utoku[0] , parametry_utoku[1] , parametry_utoku [2])
    
    while p < pocet_kol:
        p += 1

        R1_blok = 0
        R2_blok = 0
        
        R1.priprava_pozic()
        R1.obrana()
        
        R2.pos_s = rd.choice(("l","p","t","h"))
        R2.pos_d = rd.choice(("l","p","t","h"))
        R2.obrana()

        stret(R1,R2)
        
        if shozeni(R1,R2) == True:
            komentator(R1,R2,stav = "shozen")
            break
        komentator(R1, R2, stav = "probiha")
        
    komentator(R1,R2, stav = "konec")
    
### Testovani
def vitez(R1,R2):
    global a,b,c,R1_v
    if R1.s > R2.s and R1.s > 0:
        a = a + 1
        R1_v = R1_v + 1
    elif R2.s > R1.s and R2.s > 0:
        b = b + 1

    elif R1.s == R2.s or (R1.s and R2.s) <= 0:
        c = c + 1
        
def testovaci_turnaj():
    global R1_blok, R2_blok,R1_v, a, b, c, d, e, f, kombinace,Zbroj, Drevec, Kun
    index_h = 36
    iterace = 0
    
    while index_h > 35:
        parametry_z, parametry_d, parametry_k = generator()
        stat = []
        for i in range(36):
            R1_v = 0
            for k in range (36):
                R1 = Figurant("Alistar", 0, parametry_z [i] [1], 40,"l","l", parametry_z [i] [0])
                R2 = Figurant("Duncan", 0 , parametry_z [k] [1], 40,"p","p", parametry_z [k] [0])
                
                a = 0
                b = 0
                c = 0
                d = 0
                e = 0
                f = 0
                
                for j in range(3):
                   
                    R1_blok = 0
                    R2_blok = 0
                    
                    R1.utok(parametry_d [i] [1], parametry_k [i] [1], parametry_d[i] [0] + parametry_k [i] [0])
                    R2.utok(parametry_d [k] [1], parametry_k [k] [1], parametry_d[k] [0] + parametry_k [k] [0])
                    R1.obrana()
                    R2.obrana()
                    
                    stret(R1,R2)
                    
                    if R1.s <= 0 and R2.s > 0:
                        R1_v = R1_v + 1
                        break
                
                    elif R2.s <= 0 and R1.s > 0:
                        break
                        
                    elif R2.s <= 0 and R1.s <= 0:
                        break
    
                vitez(R1,R2)
                stat.append([i,R1_v])
            
        maximum = 0   
        champ = None
        for pole in stat:
            if pole[1] > maximum:
                champ = pole [0]
                maximum = pole[1]
          
        # Nejlepsi kombinace vybaveni
        Vybrana_zbroj = parametry_z [champ]
        Vybrany_drevec = parametry_d[champ]
        Vybrany_kun = parametry_k[champ]
        kombinace = [Vybrana_zbroj , Vybrany_drevec , Vybrany_kun]
        index_h = maximum
        iterace = iterace + 1
        
    print (maximum)
    print(kombinace)
    print(Zbroj)
    print(Drevec)
    print(Kun)
        
def generator():
    global Zbroj, Drevec, Kun
    # typ_zbroje = {'zadna': [0, 0], 'kozena': [-7, 8], 'krouzkova': [-8, 10], 'platova': [-20, 24]}
    # typ_drevce = {'lehky': [-3, 15], 'stredni': [-5, 20], 'tezky': [-10, 24]}
    # kun = {'cval': [0, 0], 'klus': [-4, 7], 'trysk': [-9, 10]}
    typ_zbroje, typ_drevce, kun  = generator_vybaveni()
    
    parametry_z = []
    parametry_d = []
    parametry_k = []
   
    for i in typ_zbroje.values():
        for j in typ_drevce.values():
            for k in kun.values():
                parametry_z.append(i)
                parametry_d.append(j)
                parametry_k.append(k)
     
    return parametry_z, parametry_d, parametry_k

def generator_vybaveni():
    global Zbroj, Drevec, Kun
    Zbroj = {"zadna":[0,0], "kozena":[-1*(rd.randint(2, 10)),rd.randint(5, 10)], "krouzkova":[-1*(rd.randint(4, 15)),rd.randint(9, 20)],"platova":[-1*(rd.randint(7, 20)),rd.randint(12, 25)]}
    Drevec = {"lehky":[0,rd.randint(3, 10)],"stredni":[-1*(rd.randint(4, 9)),rd.randint(8, 15)],"tezky":[-1*(rd.randint(5, 11)),rd.randint(10, 25)]}
    Kun = {"cval":[0,0],"klus":[-1*(rd.randint(1, 10)),rd.randint(2, 10)],"trysk":[-1*(rd.randint(3, 10)),rd.randint(5, 15)]}
    
    return Zbroj,Drevec,Kun
testovaci_turnaj()


