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
        
    def utok(self):
        #Vyber drevce
        drevec = input ("Zvol si drevec: ")
        typ_drevce = {"lehky":[-5,4],"stredni":[-10,6],"tezky":[-15,10]}
        #Rychlost kone
        rychlost = input("Zadej rychlost kone cval/klus/trysk: ")
        kun = {"cval":[0,0],"klus":[-3,2],"trysk":[-5,3],}
        self.pos_d = input("Kam miris drevcem H,LR,PR,T: ")
        #Vypocet utocneho cisla
        self.uc = rd.randrange(1,typ_drevce [drevec.lower()] [1] + 1) + kun[rychlost.lower()] [1]
        #Vypocet unavy
        self.s = self.s + typ_drevce [drevec.lower()] [0] + kun[rychlost.lower()] [0] + self.unava 
        
    def obrana(self):
        self.oc = self.oc + rd.randrange(0,7)
        self.pos_s = input("Pozice stitu H,LR,PR,T: ")
        

def vytvor_rytire():
    jmeno = input("Jmeno: ")
    s = int(input("Vydrz: "))
    uc = 0
    oc = 0
    pos_d =""
    pos_s = ""
    
    zbroj = input("Zadej druh zbroje - zadna,kozena,krouzkova,platova: ")
    typ_zbroje = {"zadna":[0,0], "kozena":[-3,1], "krouzkova":[-5,3],"platova":[-7,4]}
    
    unava = typ_zbroje[zbroj.lower()][0]
    oc = oc + typ_zbroje[zbroj.lower()][1]
    
    return Rytir(jmeno,uc,oc,s,pos_d,pos_s,unava)

def stret(R1,R2):
    R1.utok(), R1.obrana()
    R2.utok(), R2.obrana()
    #Zasahy
    Zasah_R1 = R2.s - R1.uc
    Zasah_R2 = R1.s - R2.uc
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
        R2.s = Zasah_R1
    #Zasah R2    
    elif R1.uc < R2.oc and R1_blok == 0:
        R1.s = Zasah_R2
    #Remiza - R1.uc == R2.oc or R2.uc == R1.uc, nebo oba rytiri utok odrazili 
    else:
        pass
    print(f"Rytíř {R1.jmeno} zaútočil silou: {R1.uc}. Výdrž po {p}. kole: {R1.s}")
    print(f"Rytíř {R2.jmeno} zaútočil silou: {R2.uc}. Výdrž po {p}. kole: {R2.s}")
    
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
    vytvor_rytire()
    
    while p < pocet_kol:
        p += 1
        stret(R1,R2)
        
        if shozeni(R1,R2) == True:
            break
        
    vitez(R1,R2)

turnaj()  

    
    

        
    
    

    
