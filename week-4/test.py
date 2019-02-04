class Õppija:
    def __init__(self, mat_nr, eesnimi, perenimi, isikukood):
        self.matrikli_nr = mat_nr
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.isikukood = isikukood

    def sugu(self):
        # Vaatleme, kas isikukoodi esimene number on paaris- või paaritu arv.
        if self.isikukood//10000000000 % 2 == 1:
            return "M"
        else:
            return "N"
    kool = "Tartu Ülikool"

    def kusÕpib():
        return "Õpib koolis "+Õppija.kool+"."

    def __str__(self):
        return "Õppija nimi: "+self.eesnimi+" "+self.perenimi+".\n"+Õppija.kusÕpib()


õppur1 = Õppija("A034", "Albert", "Paas", 34105212737)
õppur2 = Õppija("A037", "Pearu", "Murakas", 34206122154)

# print(õppur1.__str__())
# print(õppur2.__str__())

print(õppur1)
