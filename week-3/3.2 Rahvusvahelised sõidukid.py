def failist_sonastik(andmebaasi_faili_nimi):
    fail = open(andmebaasi_faili_nimi)
    riikide_nimed_sonastik = {}
    for line in fail:
        rida = line.split()
        riikide_nimed_sonastik[rida[0]] = rida[1]
    return riikide_nimed_sonastik


def tahised_nimedeks(riikide_tahised, riikide_nimed_sonastik):
    riikide_nimed = []
    for tahis in riikide_tahised:
        if tahis in riikide_nimed_sonastik:
            riikide_nimed.append(riikide_nimed_sonastik[tahis])
        else:
            riikide_nimed.append(None)
    return riikide_nimed


andmebaasi_faili_nimi = input('Sisestage andmebaasi faili nimi: ')

piiriyletajad = input('Piiriületajad: ')

for elem in (tahised_nimedeks(piiriyletajad.split(), failist_sonastik(andmebaasi_faili_nimi))):
    if elem == None:
        print('Tundmatu maa')
    else:
        print(elem)
