maatriks = [[4, 22, 32, 53, 73],
            [14, 23, 33, 57, 64],
            [30, 37, 40, 54, 64],
            [15, 17, 44, 60, 72],
            [7, 27, 43, 58, 71]]

maatriks_nurgad = [['X', 22, 32, 53, 'X'],
                   [14, 23, 33, 57, 64],
                   [30, 37, 40, 54, 64],
                   [15, 17, 44, 60, 72],
                   ['X', 27, 43, 58, 'X']]

maatriks_taismang = [['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X']]

maatriks_peadiagonaal = [['X', 22, 32, 53, 73],
                         [14, 'X', 33, 57, 64],
                         [30, 37, 'X', 54, 64],
                         [15, 17, 44, 'X', 72],
                         [7, 27, 43, 58, 'X']]

maatriks_korvaldiagonaal = [[4, 22, 32, 53, 'X'],
                            [14, 23, 33, 'X', 64],
                            [30, 37, 'X', 54, 64],
                            [15, 'X', 44, 60, 72],
                            ['X', 27, 43, 58, 71]]

maatriks_molemad_diagonaalid = [['X', 22, 32, 53, 'X'],
                                [14, 'X', 33, 'X', 64],
                                [30, 37, 'X', 54, 64],
                                [15, 'X', 44, 'X', 72],
                                ['X', 27, 43, 58, 'X']]


def voitis_nurkademangu(maatriks):
    if maatriks[0][0] == 'X' and maatriks[0][4] == 'X' and maatriks[4][0] == 'X' and maatriks[4][4] == 'X':
        return True
    return False


print(voitis_nurkademangu(maatriks_nurgad))


def x_peadiagonaalil(maatriks):
    elem_loendur = 0
    x_loendur = 0
    for rida in maatriks:
        if rida[elem_loendur] == 'X':
            x_loendur += 1
        elem_loendur += 1
    return x_loendur


def x_korvaldiagonaalil(maatriks):
    elem_loendur = 4
    x_loendur = 0
    for rida in maatriks:
        if rida[elem_loendur] == 'X':
            x_loendur += 1
        elem_loendur -= 1
    return x_loendur


def voitis_diagonaalidemangu(maatriks):

    if x_peadiagonaalil(maatriks) == 5 and x_korvaldiagonaalil(maatriks) == 5:
        return True
    return False


print('diagonaalid: ' + str(voitis_diagonaalidemangu(maatriks_molemad_diagonaalid)))


def voitis_taismangu(maatriks):
    for rida in maatriks:
        for elem in rida:
            if elem != 'X':
                return False
    return True


print(voitis_taismangu(maatriks_taismang))

# Maksimaalne failide arv: 1
# Töö liik: Individuaaltöö
# Järgnevad funktsioonid võtavad argumendiks 5 x 5 maatriksi, mis tähistab Bingo Loto tabelit ning milles iga element on kas täisarv lõigust 1 - 75 või suur trükitäht X. Täht X sümboliseerib seda, et vastav arv on mängus juba loositud.

# 1. Koostada funktsioon voitis_nurkademangu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud nurkademängu: kõik mänguvälja nurgad on loositud.

# 2. Koostada funktsioon voitis_diagonaalidemangu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud diagonaalidemängu: kõik mänguvälja diagonaalidel olevad arvud on loositud. Selleks koostada ja kasutada kahte abifunktsiooni:

# Funktsioon x_peadiagonaalil, mis võtab argumendiks mänguvälja ja tagastab selle peadiagonaalil olevate X arvu.
# Funktsioon x_korvaldiagonaalil, mis võtab argumendiks mänguvälja ja tagastab selle kõrvaldiagonaalil olevate X arvu.
# 3. Koostada funktsioon voitis_taismangu, mis tagastab tõeväärtuse vastavalt sellele, kas see mänguväli on võitnud täismängu: kõik mänguvälja arvud on loositud.

# Bingo Loto reeglitega saab täpsemalt tutvuda siin.

# Lahendamisel võite vajadusel inspiratsiooni ammutada abistavast videost.
