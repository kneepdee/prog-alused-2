def leidub_lennuplaan(lähtelinn, sihtlinn, lendude_andmebaas):
    def leidub_lennuplaan_kylastatud(lähtelinn, sihtlinn, lendude_andmebaas, kylastatud=set()):
        if lähtelinn == sihtlinn:
            return True
        else:
            kylastatud.add(lähtelinn)
            if lähtelinn in lendude_andmebaas:
                for linn in lendude_andmebaas[lähtelinn]:
                    if linn not in kylastatud:
                        return leidub_lennuplaan_kylastatud(linn, sihtlinn, lendude_andmebaas, kylastatud)
        return False
    return leidub_lennuplaan_kylastatud(lähtelinn, sihtlinn, lendude_andmebaas)


print(leidub_lennuplaan('Tallinn', 'Nice', {
      'Berliin': {'Tallinn'}, 'Tallinn': {'Berliin'}}))
# False

print(leidub_lennuplaan('Tallinn', 'Berliin', {
      'Berliin': {'London'}, 'Tallinn': {'Berliin'}}))
# True

print(leidub_lennuplaan('Tallinn', 'Nice', {'Pariis': {'London', 'Berliin', 'Nice'}, 'London': {
      'Berliin', 'Pariis'}, 'Berliin': {'London', 'Pariis', 'Tallinn'}, 'Tallinn': {'Berliin'}}))
# True
