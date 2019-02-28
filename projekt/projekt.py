import pandas as pd
import matplotlib.pyplot as plot
import random


def create_GDP_values(min, max, list_len):
    values = []
    for i in range(list_len):
        values.append(random.uniform(min, max))
    return values


andmed = pd.read_csv('./data/SN02- Heaolu kasv.csv',
                     delimiter=',', index_col='TIME')

andmed = andmed.drop(
    ['DIM1', 'Flag Codes', 'Flags'], axis=1)

skp_andmed = andmed.ix[andmed['Näitaja'] ==
                       'Sisemajanduse koguprodukt elaniku kohta, eurot']

skp_andmed.pop('Näitaja')
# skp_andmed.pop('TIME')

skp_andmed['Uus veerg'] = pd.Series(create_GDP_values(7000.0, 20000.0, 14), index=[
                                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])

andmed['Uus veerg'] = pd.Series([1, 2, 3, 4, 5, 6], index=['Lavastused', 'Teatrite arv',
                                                           '..uuslavastused', 'Etendused', 'Vaatajad, tuhat', 'Teatrisk�igud 1000 elaniku kohta'])
print(andmed)

print("Tabelis on ", skp_andmed.shape[0], " rida.")
print(skp_andmed)
print(skp_andmed.columns)

plot.plot(skp_andmed['Value'], label='Eesti')
plot.plot(skp_andmed['Uus veerg'], label='Random Generated')

# skp_andmed['Value'].plot()
plot.xlabel('Aasta')
plot.ylabel('Sisemajanduse koguprodukt elaniku kohta, eurot')
plot.title("Eesti SKP")
plot.legend()
plot.show()
