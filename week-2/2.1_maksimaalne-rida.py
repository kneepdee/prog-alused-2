faili_nimi = input('Sisestage failinimi: ')
# faili_nimi = 'arvud.txt'

fail = open(faili_nimi, encoding="UTF-8")

koik_read = []

for rida in fail:
  arr = []
  rida = rida.split(' ')
  for elem in rida:
    arr.append(int((elem.strip())))
  koik_read.append(arr)

suurim = sum(koik_read[0])
indeks = 0

for rida in koik_read:
  if sum(rida) > suurim:
    suurim = sum(rida)
    indeks = koik_read.index(rida)

print('Suurim summa on failis ' + str(indeks + 1) + '. real ja see on ' + str(suurim) + '.')

