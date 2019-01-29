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
