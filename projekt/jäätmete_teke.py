import pandas as pd
import matplotlib.pyplot as plot

jäätmete_andmed = pd.read_csv('./data/jäätmed.csv',
                              delimiter=',', index_col='Vaatlusperiood')

jäätmete_andmed = jäätmete_andmed.drop(
    ['DIM1', 'Flag Codes', 'Flags', 'TIME'], axis=1)

jäätmete_tekke_andmed = jäätmete_andmed.ix[jäätmete_andmed['Näitaja'] ==
                                           'Jäätmete teke, tuhat tonni']

jäätmete_tekke_andmed = jäätmete_tekke_andmed[4:]

jäätmete_tekke_andmed.pop('Näitaja')
