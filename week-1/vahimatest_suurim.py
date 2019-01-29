def vahimatest_suurim(maatriks):
    suurim = min(maatriks[0])
    for rida in maatriks:
        if min(rida) > suurim:
            suurim = min(rida)
    return suurim


vahimatest_suurim([[3, 0], [0, -1], [2, 1]])

vahimatest_suurim([[3, 0], [0, -1], [2, 2]])

vahimatest_suurim([[3, 0]])

vahimatest_suurim([[0], [1], [2], [3], [-1]])

vahimatest_suurim([[-1], [-4], [-5], [-6], [-8]])
