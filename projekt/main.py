import pandas as pd
import matplotlib.pyplot as plot
import numpy as np


def loo_dataframe(failinimi, näitaja):
    andmed = pd.read_csv('./data/' + failinimi,
                         delimiter=',', index_col='Vaatlusperiood')

    näitajapõhised_andmed = andmed.ix[andmed['Näitaja'] ==
                                      näitaja]

    näitajapõhised_andmed = näitajapõhised_andmed.drop(
        ['DIM1', 'Flag Codes', 'Flags', 'Näitaja'], axis=1)

    if näitajapõhised_andmed['TIME'].iloc[0] < 2004:
        näitajapõhised_andmed = näitajapõhised_andmed[4:]

    return näitajapõhised_andmed


def korruta_tulba_väärtused(df_column, kordaja):
    return np.multiply(
        df_column, kordaja)


skp_andmed = loo_dataframe('SN02- Heaolu kasv.csv',
                           'Sisemajanduse koguprodukt elaniku kohta, eurot')

põllumajandusmaa_andmed = loo_dataframe(
    'bioloogilise_mitmekesisuse_vahenemine.csv', 'Intensiivpõllumajanduse kasutuses olev maa, % territooriumist')

põllumajandusmaa_andmed['Value'] = korruta_tulba_väärtused(
    põllumajandusmaa_andmed['Value'], 2500)

jäätmete_tekke_andmed = loo_dataframe(
    'jäätmed.csv', 'Jäätmete teke, tuhat tonni')

sisevete_kalapüügi_andmed = loo_dataframe(
    'bioloogilise_mitmekesisuse_vahenemine.csv', 'Sisevete kalapüük, tonni')

sisevete_kalapüügi_andmed['Value'] = korruta_tulba_väärtused(
    sisevete_kalapüügi_andmed['Value'], 6)

plot.plot(skp_andmed['Value'],
          label='Sisemajanduse koguprodukt elaniku kohta, eurot')
plot.plot(jäätmete_tekke_andmed['Value'], label='Jäätmete teke, tuhat tonni')
plot.plot(sisevete_kalapüügi_andmed['Value'],
          label='Sisevete kalapüük, 1/6 tonni')
plot.plot(põllumajandusmaa_andmed['Value'],
          label='Intensiivpõllumajanduse kasutuses olev maa, 1/2500% territooriumist')

# plot.legend()
plot.show()
