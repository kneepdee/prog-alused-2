def seosta_lapsed_ja_vanemad(laste_faili_nimi, nimede_faili_nimi):
    lapsed_fail = open(laste_faili_nimi)
    nimed_fail = open(nimede_faili_nimi)
    suhted = {}
    laste_nimed = set()

    nimed = {}

    for rida in nimed_fail:
        isikukood = rida.split()[0]
        nimi_listina = rida.split()[1:]
        nimi = ' '.join(nimi_listina)
        nimed[isikukood] = nimi

    for rida in lapsed_fail:
        vanem = nimed[rida.split()[0]]
        laps = nimed[rida.split()[1]]
        if vanem in suhted:
            suhted[vanem].add(laps)
        else:
            suhted[vanem] = set()
            suhted[vanem].add(laps)

    return suhted


# print(seosta_lapsed_ja_vanemad('./week-6/lapsed.txt', './week-6/nimed.txt'))

# {'Peeter Peedumets': {'Maria Peedumets', 'Robert Peedumets'},
# 'Madli Peedumets': {'Maria Peedumets', 'Robert Peedumets'},
# 'Karl Peedumets': {'Peeter Peedumets'},
# 'Kadri Kalkun': {'Liisa Maria Jaaniste'}}
