class Rytir():
    def __init__(self,jmeno,uc,oc,s,vaha):
        self.jmeno = jmeno
        self.uc = uc
        self.oc = oc
        self.s = s
        self.unava = unava #Unava bude kazde kolo snizovat vydrz

   
def vytvor_rytire():
    jmeno = input("Jmeno: ")
    s = input("Vydrz: ")
    uc = 0
    oc = 0
    
    zbroj = input("Zadej druh zbroje - Zadna,Kozena,Krouzkova,Platova: ")
    typ_zbroje = {"Zadna":[0,0], "Kozena":[-3,1], "Krouzkova":[-5,3],"Platova":[-7,4]}
    
    unava = typ_zbroje[zbroj][0]
    oc = oc + typ_zbroje[zbroj][1]
    
    return Rytir(jmeno,uc,oc,s,unava)


def parametry_kola():
    rychlost = input("Zadej rychlost kone cval/klus/trysk: ")
    kun = {"cval":[0,0],"klus":[-3,2],"trysk":[-5,3],}
    
    drevec = input ("Zvol si drevec: ")
    typ_drevce = {"lehky":[-5,4],"stredni":[-10,6],"tezky":[-15,10]}
    d_pos = input("Pozice drevce")
    #Rozmyslet kam zaradit utok a obranu (metoda tridy nebo funkce)
    
    """
    Pro oba rytíře:
    Zvolit váhu dřevce
    Zvolit rychlost koně
    Zvolit pozici dřevce
    Zvolit pozici štítu
    """
    
def stret():
    
    """
    Zkontrolovat pozice dřevce R1 a R2
    Zkontrolovat pozici štítu R1 a R2
    Porovnat obranné a útočné číslo R1 a R2
    Zkontrolovat výdrže
    Určit vítěze
    """
    
def turnaj():
    def vytvor_rytire():
    p =#pocet kol
    
    for i in range(1,p+1):
        def parametry_kola():
        def stret():
        
        
        
    
    

        
    
    

    
