class Õppija:
    kool = "Tartu Ülikool"
    def kusÕpib():
        return "Õpib koolis "+Õppija.kool+"."
    def __init__(self, mat_nr, eesnimi, perenimi, isikukood):
        self.matrikli_nr = mat_nr
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.isikukood = isikukood
    def __str__(self):
        return "Õppija nimi: "+self.eesnimi+" "+self.perenimi+".\n"+Õppija.kusÕpib()
    def arvuta(a,b):
        return a+b
    def sugu(self):
        if self.isikukood//10000000000%2 == 1:
            return "M"
        else:
            return "N"
#Konstruktori kasutus
õppur1 = Õppija("A034", "Albert", "Paas", 34105212737)
õppur2 = Õppija("A037", "Pearu", "Murakas", 34206122154)
 
#Isendimuutuja tekitamine/muutmine
õppur1.lemmikloom = "koer"
print(õppur1.lemmikloom)
 
#Isendispetsiifiline funktsioon
print(õppur1.sugu())
 
#Väljastamine, kasutades isendispetsiifilist funktsiooni koos staatilise muutuja ja funktsiooniga
print(õppur1)
print(õppur2)
 
#Muu staatilise funktsiooni kasutus
print(Õppija.arvuta(1,2))