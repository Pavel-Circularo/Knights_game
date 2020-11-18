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
    R1.utok()
    R1.obrana()
    
    R2.utok()
    R2.obrana()

    if R1.pos_s == R2.pos_d:
        print(f"Rytíř {R1.jmeno} odrazil útok štítem")
    #Zasah R1    
    if R1.uc > R2.oc:
        R2.s = R2.s - R1.uc
    #Zasah R2    
    elif R1.uc < R2.oc:
        R1.s = R1.s - R1.uc
    #Remiza - R1.uc == R2.oc or R2.uc == R1.uc 
    else:
        pass
    print(R1.uc,R1.oc,R1.s,R2.uc,R2.oc,R2.s)
    

R1 = vytvor_rytire()
R2 = vytvor_rytire()

stret(R1,R2)
    
    

        
    
    

    
