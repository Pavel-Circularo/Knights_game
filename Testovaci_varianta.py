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
        typ_drevce = {"lehky":[-5,4],"stredni":[-10,6],"tezky":[-15,10]}
        #Rychlost kone
        kun = {"cval":[0,0],"klus":[-3,2],"trysk":[-5,3],}
        self.pos_d = "LR"
        #Vypocet utocneho cisla
        self.uc = rd.randrange(1,typ_drevce ["stredni"] [1] + 1) + kun["klus"] [1]
        #Vypocet unavy
        self.s = self.s + typ_drevce ["stredni"] [0] + kun["klus"] [0] + self.unava 
        
    def obrana(self):
        self.oc = self.oc + rd.randrange(0,7)
        #self.pos_s = input("Pozice stitu H,LR,PR,T: ")
        self.pos_s = "H"
        
class Rytir_A(Rytir):
        
    def utok(self):
        #Vyber drevce
        typ_drevce = {"lehky":[-5,4],"stredni":[-10,6],"tezky":[-15,10]}
        #Rychlost kone
        kun = {"cval":[0,0],"klus":[-3,2],"trysk":[-5,3],}
        self.pos_d = "LR"
        #Vypocet utocneho cisla
        self.uc = rd.randrange(1,typ_drevce ["stredni"] [1] + 1) + kun["klus"] [1]
        #Vypocet unavy
        self.s = self.s + typ_drevce ["stredni"] [0] + kun["klus"] [0] + self.unava 


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
        R1_blok = 1
        
    if R2.pos_s == R1.pos_d:
        R2_blok = 1
        
    #Zasah R1    
    if R1.uc > R2.oc and R2_blok == 0:
         R2.s = R2.s - R1.uc
         
    #Zasah R2    
    if R2.uc > R1.oc and R1_blok == 0:
        R1.s = R1.s - R2.uc
        
    if ((R1.uc  <= R2.oc) and (R2.uc <= R1.uc)) or (R1_blok == 1 and R2_blok == 1):
        pass
    
#Určení vítěze    
def vitez(R1,R2):
    global a,b,c
    
    if R1.s > R2.s and R1.s > 0:
        a = a + 1 
        
    elif R2.s > R1.s and R2.s > 0:
        b = b + 1
        
    elif R1.s == R2.s or (R1.s and R2.s) <= 0:
        c = c + 1
#Kontrola shození před koncem turnaje        
def shozeni(R1,R2):
    if R1.s <= 0 and R2.s > 0:
        return True
    
    elif R2.s <= 0 and R1.s > 0:
        return True
        
    elif R2.s <= 0 and R1.s <= 0:
        return True
    
#Hlavní program   
def turnaj():
    global p
    p = 0
    pocet_kol = 3
    R1 = Rytir("Alistar",0,0,70,"","",0)
    R2 = Rytir_A("Duncan",0,0,70,"","",0)
    
    while p < pocet_kol:
        p += 1
        stret(R1,R2)
        
        if shozeni(R1,R2) == True:
            break
        
    vitez(R1,R2)
    
    
def test():
    global a,b,c
    pocet_spusteni = 1000
    
    a = 0 #Vyhra R1
    b = 0 #Vyhra R2
    c = 0 #Remiza

    for i in range (0,pocet_spusteni):
        turnaj()  
    print(f"Počet výher R1: {a}, počet výher R2: {b}, počet remíz: {c}")
        
test()
