maatriks1 = [['ab', 'ba']]
# >>> leidub_anagramm([['ab', 'ba']])
# True

maatriks2 = [['ab', 'cad', 'cd'], ['abd', 'a', 'bd']]
# >>> leidub_anagramm([['ab', 'cad', 'cd'], ['abd', 'a', 'bd']])
# False

maatriks3 = [['ab', 'cad', 'cd'], ['a', 'bad', 'bd']]
# >>> leidub_anagramm([['ab', 'cad', 'cd'], ['a', 'bad', 'bd']])
# True


def leidub_anagramm(maatriks):
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            s = ''
            if j > 0:
                s += maatriks[i][j - 1]
            if j < len(maatriks[i]) - 1:
                s += maatriks[i][j + 1]
            if sorted(s) == sorted(maatriks[i][j]):
                return True
    return False


print(leidub_anagramm(maatriks1))
print(leidub_anagramm(maatriks2))
print(leidub_anagramm(maatriks3))