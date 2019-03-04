import pandas as pd
import matplotlib.pyplot as plot
import numpy as np


def loo_dataframe(failinimi, näitaja):
    andmed = pd.read_csv('./data/' + failinimi,
                         delimiter=',', index_col='Vaatlusperiood')

    # jätame df-i alles ainult meid huvitavale näitajale vastavad andmed
    näitajapõhised_andmed = andmed.ix[andmed['Näitaja'] ==
                                      näitaja]

    # vabaneme nendest tulpadest, mida vaja ei ole
    näitajapõhised_andmed = näitajapõhised_andmed.drop(
        ['DIM1', 'Flag Codes', 'Flags', 'Näitaja'], axis=1)

    # alustame df-i aastast 2004, et plotid ilusad välja näeksid
    näitajapõhised_andmed = näitajapõhised_andmed[pd.Index(
        list(näitajapõhised_andmed['TIME'])).get_loc(2004):]

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

f_gaaside_heitekogus_andmed = loo_dataframe(
    'kliimamuutus.csv', 'F-gaaside heitkogus, CO2 ekvivalenttonni')

f_gaaside_heitekogus_andmed['Value'] = korruta_tulba_väärtused(
    f_gaaside_heitekogus_andmed['Value'], 105)

# plot.plot(skp_andmed['Value'],
#           label='Sisemajanduse koguprodukt elaniku kohta, eurot')
# plot.plot(jäätmete_tekke_andmed['Value'], label='Jäätmete teke, tuhat tonni')
# plot.plot(sisevete_kalapüügi_andmed['Value'],
#           label='Sisevete kalapüük, 1/6 tonni')
# plot.plot(põllumajandusmaa_andmed['Value'],
#           label='Intensiivpõllumajanduse kasutuses olev maa, 1/2500% territooriumist')
# plot.plot(f_gaaside_heitekogus_andmed['Value'],
#           label='F-gaaside heitkogus, CO2 ekvivalenttonni')

# plot.legend()
# plot.show()

# todo: funktsioon, mis automaatselt scalib väärtused skt kõveraga sobivale skaalale
# todo: kliimamuutusest f-gaaside heitekoguse andmed
