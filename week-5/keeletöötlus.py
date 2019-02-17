def eemaldaPunktuatsioon(tekst):
    tekst = tekst.replace(".", "")
    tekst = tekst.replace(",", "")
    tekst = tekst.replace("!", "")
    tekst = tekst.replace("?", "")
    return tekst
 
eesti_keele_sagedasemad = []
# Avame eesti keele sagedasemate sõnavormide faili
fail = open("eesti_keele_sonavormid.txt", "r", encoding="utf-8")
for rida in fail:
    # Tükeldame rea tühiku järgi, failis on esimesel kohal sõnavormi sagedus,
    # teisel kohal sõnavorm ise
    rida = rida.split()
    eesti_keele_sagedasemad.append(rida[1])
    # Võtame arvesse vaid sagedasemaid eesti keele sõnavorme
    if len(eesti_keele_sagedasemad) > 200:
        break
fail.close()
#print(eesti_keele_sagedasemad)
 
 
# Avame faili
fail = open("valton_kanaromaan.txt", "r", encoding="utf-8")
 
# Sõnastik sõnavormide jaoks
sonavormid = {}
 
for rida in fail:
    # Eemaldame reavahetused jms rea algusest ja lõpust
    rida = rida.strip()
    # Väiketähestame teksti
    rida = rida.lower()
    # Eemaldame punktuatsiooni
    rida = eemaldaPunktuatsioon(rida)
    # Töötleme rida sel juhul, kui see pole tühi
    if rida != "":
        # Tükeldame rea tühikute kohalt sõnedeks
        sonad = rida.split()
        # Kui sellise võtmega elementi sõnastikus veel pole,
        # lisame selle koos väärtusega 1
        # (selleks momendiks on seda vormi esinenud tekstis 1 kord),
        # kui aga on, suurendame selle võtmega elemendi väärtust ühe võrra
        for sona in sonad:
            # Lisame sagedusloendisse vaid sõnad, mis ei esine
            if sona not in eesti_keele_sagedasemad:
                if sona not in sonavormid:
                    sonavormid[sona] = 1
                else:
                    sonavormid[sona] += 1
 
# Sulgeme faili
fail.close()
 
print("Sõnavormide arv:", len(sonavormid))
 
loendur = 1
for vorm in sorted(sonavormid, key=sonavormid.get, reverse=True):
    print(loendur, vorm, sonavormid[vorm])
    loendur += 1
    if loendur > 30:
        break