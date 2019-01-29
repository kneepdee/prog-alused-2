def on_bingo_tabel(maatriks):
    for rida in maatriks:
        if rida[0] >= 1 and rida[0] <= 15 and rida[1] >= 16 and rida[1] <= 30 and rida[2] >= 31 and rida[2] <= 45 and rida[3] >= 46 and rida[3] <= 60 and rida[4] >= 61 and rida[4] <= 75:
            valid_tabel = True
        else:
            valid_tabel = False
            break

    return valid_tabel


bingo_maatriks = [[1, 30, 34, 55, 75], [10, 16, 40, 50, 67], [
    5, 20, 38, 48, 61], [4, 26, 43, 49, 70], [15, 17, 33, 51, 66]]

maatriks2 = [[4, 22, 32, 53, 73],
             [14, 23, 33, 57, 64],
             [30, 37, 40, 54, 64],
             [15, 17, 44, 60, 72],
             [7, 27, 43, 58, 71]]

print(on_bingo_tabel(bingo_maatriks))
print(on_bingo_tabel(maatriks2))

print(maatriks2[2][0] >= 1 and maatriks2[2][0] <= 15)

# Et tegu oleks korrektse Bingo Loto mänguväljaga,
# peavad vasakpoolseimas veerus olevad arvud kuuluma lõiku 1 - 15,
# järgmises veerus olevad arvud lõiku 16 - 30 ja nii edasi,
# kuni viimases veerus on ainult arvud lõigust 61 - 75.
