def opi(x_list, y_list):
    # Modelleerime sõltuvust sisendi ja väljundi vahel
    # lineaarfunktsiooni (sirge) abil: valjund = a * sisend + b, kus
    # a ja b on kordajad ehk kaalud ehk mudeli parameetrid.
    # Kordajate arvutamiseks kasutame sirge võrrandit kahe punktiga.
    # Kuna sirge on määratud kahe punktiga, siis õppimiseks rakendamegi
    # ainult kahte esimest näidet isegi siis, kui neid on antud rohkem.
 
    a = (y_list[1] - y_list[0]) / (x_list[1] - x_list[0])
    b = (y_list[0] * x_list[1] - y_list[1] * x_list[0]) / (x_list[1] - x_list[0])
    return [a, b]  # Tagastame kordajad listina
 
def ennusta(x, kaalud):
    # Ennustamiseks on vaja arvutada lineaarfunktsiooni väärtus
    # kohal x, mis vastab kasutaja sisendile, kasutades õpitud kordajaid.
    a = kaalud[0]
    b = kaalud[1]
    return a * x + b
 
# Loeme treeningandmed failist.
f = open('treeningandmed.txt')
sisendvaartused = []
valjundvaartused = []
for rida in f:
    jupid = rida.split(',')
    sisendvaartused.append(float(jupid[0]))
    valjundvaartused.append(float(jupid[1]))
f.close()
 
# Õpime treeningandmete põhjal selgeks kaalud ehk mudeli parameetrid.
kaalud = opi(sisendvaartused, valjundvaartused)
 
# Ennustame uue sisendi väärtust, kasutades õpitud kaale.
kasutaja_sisend = float(input('Sisend: '))
ennustus = ennusta(kasutaja_sisend, kaalud)
print('Ennustus: ' + str(ennustus))