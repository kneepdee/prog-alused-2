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

jäätmete_tekke_andmed = loo_dataframe(
    'jäätmed.csv', 'Jäätmete teke, tuhat tonni')

sisevete_kalapüügi_andmed = loo_dataframe(
    'bioloogilise_mitmekesisuse_vahenemine.csv', 'Sisevete kalapüük, tonni')

f_gaaside_heitekogus_andmed = loo_dataframe(
    'kliimamuutus.csv', 'F-gaaside heitkogus, CO2 ekvivalenttonni')

skp_min = skp_andmed['Value'].min()

andmed_dict = {
    'skp': [skp_andmed],
    'põllumajandus': [põllumajandusmaa_andmed],
    'jäätmete teke': [jäätmete_tekke_andmed],
    'kalapüük': [sisevete_kalapüügi_andmed],
    'f-gaasid': [f_gaaside_heitekogus_andmed]
}

# print(andmed_dict['Sisemajanduse koguprodukt elaniku kohta, eurot'][0])

for key, value in andmed_dict.items():
    multiplier = str(round(skp_min / value[0]['Value'].iloc[0], 2))
    value.append(multiplier)
    print(value[1])
    value[0]['Value'] = korruta_tulba_väärtused(
        value[0]['Value'], skp_min / value[0]['Value'].iloc[0])

print(andmed_dict)

plot.plot(skp_andmed['Value'],
          label='Sisemajanduse koguprodukt elaniku kohta, ' + andmed_dict['skp'][1] + ' eurot')
plot.plot(jäätmete_tekke_andmed['Value'], label='Jäätmete teke, ' +
          andmed_dict['jäätmete teke'][1] + ' tuhat tonni')
plot.plot(sisevete_kalapüügi_andmed['Value'],
          label='Sisevete kalapüük, ' + andmed_dict['kalapüük'][1] + ' tonni')
plot.plot(põllumajandusmaa_andmed['Value'],
          label='Intensiivpõllumajanduse kasutuses olev maa, 1/' + andmed_dict['põllumajandus'][1] + '% territooriumist')
plot.plot(f_gaaside_heitekogus_andmed['Value'],
          label='F-gaaside heitkogus, ' + andmed_dict['f-gaasid'][1] + ' CO2 ekvivalenttonni')

plot.legend()
plot.show()

# todo:

# funktsioon, mis automaatselt scalib väärtused skt kõveraga sobivale skaalale, niiet kõik jooned alagavad samast kohast
# lisaks annab ka legendile õige väärtuse/ühiku, mida plotil näidata

# küsib kasutajalt, milliseid plote ta näha tahab ja väljastab sellise ploti, millel on ainult need nõutud jooned. kasuta selleks nt array data type'i.
