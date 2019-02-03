def kooslubajad(erakondade_lubadused):
    suurima_yhisosaga_erakondade_indeksid = (0, 1)
    for erakond in erakondade_lubadused:
        for erakond2 in erakondade_lubadused:
            if erakondade_lubadused.index(erakond) != erakondade_lubadused.index(erakond2):
                if len(erakond & erakond2) > len(erakondade_lubadused[suurima_yhisosaga_erakondade_indeksid[0]] & erakondade_lubadused[suurima_yhisosaga_erakondade_indeksid[1]]):
                    suurima_yhisosaga_erakondade_indeksid = (
                        erakondade_lubadused.index(erakond), erakondade_lubadused.index(erakond2))
    print(suurima_yhisosaga_erakondade_indeksid)
    return suurima_yhisosaga_erakondade_indeksid

kooslubajad([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"}, {"lasteaiaõpetajate palku tõsta",
                                                                             "kindlustada tasuta hambaravi kuni 30-aastastele"}, {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"}, set()])
# (0, 2)

kooslubajad([{"arstide palku tõsta", "pensione tõsta", "kaitsekulutusi tõsta"}, {"lasteaiaõpetajate palku tõsta", "motosporti toetada"}, {"sisserännet piirata", "pensione tõsta", "arstide palku tõsta",
                                                                                                                                          "lasteaiaõpetajate palku tõsta"}, {"arstide palku tõsta", "tuletõrjujate palku tõsta", "politseinike palku tõsta", "piirivalvurite palku tõsta", "vangivalvurite palku tõsta"}])
# (0, 2)

kooslubajad([{"algatada koduloometoetus", "kuritegevust vähendada", "kõiki toetusi suurendada", "kaotada kõik maksud", "suurendada kõigi palkasid",
              "rajada spordiväljakud igasse linna"}, {"toetada pensionäre", "aidata noorperesid", "edendada maaelu", "suurendada vastsündinute arvu", "vähendada suremust"}])
# (0, 1)
