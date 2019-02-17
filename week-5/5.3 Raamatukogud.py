import pandas as pd
import matplotlib.pyplot as plot

# andmed = pd.read_csv('raamatukogud.csv', delimiter=';', index_col=' ')

def taienda_tabelit(tabel):
    tabel.pop('2012')
    tabel['Keskmine'] = pd.Series([tabel.loc['Raamatukogud'].mean(), tabel.loc['Lugejad, tuhat'].mean(), tabel.loc['Lugejaid keskmiselt raamatukogu kohta'].mean(), tabel.loc['Laenutusi keskmiselt lugeja kohta, arvestusuksust'].mean(), tabel.loc['Tootajad'].mean()], index=['Raamatukogud', 'Lugejad, tuhat', 'Lugejaid keskmiselt raamatukogu kohta', 'Laenutusi keskmiselt lugeja kohta, arvestusuksust', 'Tootajad'])

    return tabel

print(taienda_tabelit(andmed))

def raamatukogud(csv_fail_laiendiga):
  andmed = pd.read_csv(csv_fail_laiendiga, delimiter=';', index_col=' ')
  uued_andmed = taienda_tabelit(andmed)
  uued_andmed.to_csv(csv_fail_laiendiga.replace('.csv', '_uus.csv'), sep=';', encoding='utf-8')

raamatukogud('raamatukogud.csv')