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
        
    def priprava(self):
        #Parametry vybavení
        typ_drevce = {"lehky":[-5,4],"stredni":[-10,6],"tezky":[-15,10]}
        kun = {"cval":[0,0],"klus":[-3,2],"trysk":[-5,3]}
        #Vyber drevce
        while True:
            drevec = (input ("Zvol si drevec lehky/stredni/tezky: ")).lower()
            if drevec not in typ_drevce.keys():
                print("Spatne zadany drevec")
                continue
            else:
                self.kostka_uc = typ_drevce [drevec] [1]
                self.unava = self.unava + typ_drevce [drevec] [0]
                break
                
        while True:
            rychlost = (input("Zadej rychlost kone cval/klus/trysk: ")).lower()
            if rychlost not in kun.keys():
                print("Spatne zadana rychlost")
                continue
            
            else:
                self.rychlost_uc = kun [rychlost] [1]
                self.unava = self.unava + kun [rychlost] [0]
                break
                
        while True:
            pozice_drevce = (input("Kam miris drevcem H,L,P,T:")).lower()
            if pozice_drevce not in "h,l,p,t":
                print("Spatne zadana pozice drevce")
                continue
            else:
                self.pos_d = pozice_drevce
                break
                
        while True:
            pozice_stitu = (input("Pozice stitu H,L,P,T:")).lower()
            if pozice_stitu not in "h,l,p,t":
                print("Spatne zadana pozice stitu")
                continue
            else:
                self.pos_s = pozice_stitu
                break
        
        #Vypocet unavy
        self.s = self.s + self.unava
       
    def utok(self):
        #Vypocet utocneho cisla
        self.uc = rd.randrange(1,self.kostka_uc + 1) + self.rychlost_uc

    def obrana(self):
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
  
def stret(R1,R2):
    #Nastaveni utocnych a obrannych cisel
    R1.utok()
    R1.obrana()
    R2.utok()
    R2.obrana()

    #Blokovani stitem
    R1_blok = 0
    R2_blok = 0

    if R1.pos_s == R2.pos_d:
        print(f"Rytíř {R1.jmeno} odrazil útok štítem")
        R1_blok = 1
        
    if R2.pos_s == R1.pos_d:
        print(f"Rytíř {R2.jmeno} odrazil útok štítem")
        R2_blok = 1
        
    #Zasah R1    
    if R1.uc > R2.oc and R2_blok == 0:
         R2.s = R2.s - R1.uc
         print(f"Rytíř {R1.jmeno} překonal silou: {R1.uc}, obranu soupeře {R2.oc}.")
         
    #Zasah R2    
    if R2.uc > R1.oc and R1_blok == 0:
        R1.s = R1.s - R2.uc
        print(f"Rytíř {R2.jmeno} překonal silou: {R2.uc}, obranu soupeře: {R1.oc}.")
        
    if ((R1.uc  <= R2.oc) and (R2.uc <= R1.uc)) or (R1_blok == 1 and R2_blok == 1) :
        print("Rytíři se ubránili soupeři")

#Určení vítěze    
def vitez(R1,R2):
    if R1.s > R2.s and R1.s > 0:
        print(f"Zvítězil rytíř {R1.jmeno}")

        
    elif R2.s > R1.s and R2.s > 0:
        print(f"Zvítězil rytíř {R2.jmeno}")

        
    elif R1.s == R2.s or (R1.s and R2.s) <= 0:
        print("Remíza")

#Kontrola shození před koncem turnaje        
def shozeni(R1,R2):
    if R1.s <= 0 and R2.s > 0:
        print(f"Rytíř {R1.jmeno} je shozen ze sedla v {p}. kole")
        return True
    
    elif R2.s <= 0 and R1.s > 0:
        print(f"Rytíř {R2.jmeno} je shozen ze sedla v {p}. kole")
        return True
        
    elif R2.s <= 0 and R1.s <= 0:
        print(f"Oba rytíři jsou shozeni ze sedla v {p}. kole")
        return True
    
#Hlavní program   
def turnaj():
    global p
    p = 0
    pocet_kol = 3
    R1 = vytvor_rytire()
    R2 = vytvor_rytire()
    # R1 = Rytir("Alistar",0,0,100,"","",0)
    # R2 = Rytir("Duncan",0,0,100,"","",0)
    
    while p < pocet_kol:
        p += 1
        print(20*"-"+f" KOLO {p} "+20*"-")
        
        R1.priprava()
        R2.priprava()
        stret(R1,R2)
        
        if shozeni(R1,R2) == True:
            break
        
        if R1.s > 0 and R2.s > 0: 
            print(f"Rytíř {R1.jmeno} nastupuje do {p+1}. kola s výdrží: {R1.s}")
            print(f"Rytíř {R2.jmeno} nastupuje do {p+1}. kola s výdrží: {R2.s}")
    
    vitez(R1,R2)

turnaj()

    
    

        
    
    

    
