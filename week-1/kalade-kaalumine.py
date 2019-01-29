def kala_kaal(kala_pikkus, kalaliigi_tysedusindeks):
    return round((kala_pikkus ** 3) * kalaliigi_tysedusindeks / 100)


print(kala_kaal(70, 0.19))

print(kala_kaal(12, 1.34))

# failinimi = 'kalad.txt'
failinimi = input('Sisestage failinimi: ')

# pyygi_alammoot = 55
pyygi_alammoot = int(input('Sisestage püügi alammõõt: '))

# tysedusindeks = 0.19
tysedusindeks = float(input('Sisestage Fultoni tüsedusindeks: '))

fail = open(failinimi)

kalade_kaalud = []

for kala_pikkus in fail:
    if int(kala_pikkus) < pyygi_alammoot:
        print('Kala lasti vette tagasi')
    else:
        kalade_kaalud.append(kala_kaal(int(kala_pikkus), tysedusindeks));
        print('Püütud kala kaaluga ' + str(kala_kaal(int(kala_pikkus), tysedusindeks)) + ' grammi')

print('Kõige raskem püütud kala: ' + str(max(kalade_kaalud) / 1000) + 'kg')
