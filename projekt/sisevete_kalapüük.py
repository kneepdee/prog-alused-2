import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

bioloogilise_mitmekesisuse_vahenemine = pd.read_csv('./data/bioloogilise_mitmekesisuse_vahenemine.csv',
                                                    delimiter=',', index_col='Vaatlusperiood')

bioloogilise_mitmekesisuse_vahenemine = bioloogilise_mitmekesisuse_vahenemine.drop(
    ['DIM1', 'Flag Codes', 'Flags', 'TIME'], axis=1)

sisevete_kalapüügi_andmed = bioloogilise_mitmekesisuse_vahenemine.ix[bioloogilise_mitmekesisuse_vahenemine['Näitaja'] ==
                                                                     'Sisevete kalapüük, tonni']

sisevete_kalapüügi_andmed = sisevete_kalapüügi_andmed[4:]

sisevete_kalapüügi_andmed.pop('Näitaja')


def korruta_tulba_väärtused(df_column, kordaja):
    return np.multiply(
        df_column, kordaja)


sisevete_kalapüügi_andmed['Value'] = korruta_tulba_väärtused(
    sisevete_kalapüügi_andmed['Value'], 6)

print(sisevete_kalapüügi_andmed)
