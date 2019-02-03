from random import sample


def on_bingo_tabel(maatriks):
    for rida in maatriks:
        if rida[0] >= 1 and rida[0] <= 15 and rida[1] >= 16 and rida[1] <= 30 and rida[2] >= 31 and rida[2] <= 45 and rida[3] >= 46 and rida[3] <= 60 and rida[4] >= 61 and rida[4] <= 75:
            valid_tabel = True
        else:
            valid_tabel = False
            break

    return valid_tabel


def juhuslik_bingo():
    bingo_tabel = [[], [], [], [], []]
    start = 1
    end = 16
    for i in range(5):
        column = sample(range(start, end), 5)
        bingo_tabel[0].append(column[0])
        bingo_tabel[1].append(column[1])
        bingo_tabel[2].append(column[2])
        bingo_tabel[3].append(column[3])
        bingo_tabel[4].append(column[4])

        start += 15
        end += 15

    return bingo_tabel


print(juhuslik_bingo())
