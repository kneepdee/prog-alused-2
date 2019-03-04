import pandas as pd
import matplotlib.pyplot as plot
import random
from jäätmete_teke import *
from sisevete_kalapüük import *
from põllumajanduses_kasutuses_olev_maa import *

heaolu_andmed = pd.read_csv('./data/SN02- Heaolu kasv.csv',
                            delimiter=',', index_col='Vaatlusperiood')

heaolu_andmed = heaolu_andmed.drop(
    ['DIM1', 'Flag Codes', 'Flags', 'TIME'], axis=1)

skp_andmed = heaolu_andmed.ix[heaolu_andmed['Näitaja'] ==
                              'Sisemajanduse koguprodukt elaniku kohta, eurot']

skp_andmed.pop('Näitaja')

# print("Tabelis on ", skp_andmed.shape[0], " rida.")
# print(skp_andmed)
# print(skp_andmed.columns)

plot.plot(skp_andmed['Value'],
          label='Sisemajanduse koguprodukt elaniku kohta, eurot')
plot.plot(jäätmete_tekke_andmed['Value'], label='Jäätmete teke, tuhat tonni')
plot.plot(sisevete_kalapüügi_andmed['Value'],
          label='Sisevete kalapüük, 1/6 tonni')
plot.plot(põllumajandusmaa_andmed['Value'],
          label='Intensiivpõllumajanduse kasutuses olev maa, 1/2500% territooriumist')

plot.legend()
plot.show()
