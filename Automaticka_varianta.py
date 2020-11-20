import random as rd

#Testovaci varianta bez přístupu uživatele
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
        #drevec = input ("Zvol si drevec: ")-10
        typ_drevce = {"lehky":[-5,4],"stredni":[0,6],"tezky":[-15,10]}
        #Rychlost kone
        #rychlost = input("Zadej rychlost kone cval/klus/trysk: ") -3
        kun = {"cval":[0,0],"klus":[0,2],"trysk":[-5,3],}
        #self.pos_d = input("Kam miris drevcem H,LR,PR,T: ")
        self.pos_d = "LR"
        #Vypocet utocneho cisla
        self.uc = rd.randrange(1,(typ_drevce ["stredni"] [1]) + 1) + kun["klus"] [1]
        #Vypocet unavy
        self.s = self.s + typ_drevce ["stredni"] [0] + kun["klus"] [0] + self.unava 
        
    def obrana(self):
        self.oc = self.oc + rd.randrange(0,7)
        #self.pos_s = input("Pozice stitu H,LR,PR,T: ")
        self.pos_s = "H"
  
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
         print(f"Rytíř {R1.jmeno} překonal silou: {R1.uc}, obranu soupeře {R2.oc}. Výdrž po {p}. kole: {R1.s}")
         
    #Zasah R2    
    if R2.uc > R2.oc and R1_blok == 0:
        R1.s = R1.s - R2.uc
        print(f"Rytíř {R2.jmeno} překonal silou: {R2.uc}, obranu soupeře: {R1.oc}. Výdrž po {p}. kole: {R2.s}")
    else:
        print("Rytíři se střetli se stejnou silou")
        print(f"Rytíř {R1.jmeno} výdrž {R1.s} po {p}. kole")
        print(f"Rytíř {R2.jmeno} výdrž {R2.s} po {p}. kole")
    #Remiza - R1.uc == R2.oc or R2.uc == R1.uc, nebo oba rytiri utok odrazili 


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
    #vytvor_rytire():
    R1 = Rytir("Alistar",0,0,70,"","",0)
    R2 = Rytir("Duncan",0,0,70,"","",0)
    
    while p < pocet_kol:
        p += 1
        print(f"----------KOLO {p}----------")
        stret(R1,R2)
        
        if shozeni(R1,R2) == True:
            break
        
    vitez(R1,R2)

turnaj()
    
