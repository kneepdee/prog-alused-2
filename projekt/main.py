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

for key, value in andmed_dict.items():
    multiplier = str(round(1 / (skp_min / value[0]['Value'].iloc[0]), 4))
    value.append(multiplier)
    value[0]['Value'] = korruta_tulba_väärtused(
        value[0]['Value'], skp_min / value[0]['Value'].iloc[0])


def kasutaja_sisend_järjendiks(sisend):
    sisend_array = sisend.split(',')
    sisend_array_trimmed_ints = []
    for element in sisend_array:
        element_stripped = element.strip()
        try:
            element_stripped_int = int(element_stripped)
        except ValueError:
            print(element_stripped + ' ei ole number. Sisesta ainult numbreid.')
            continue
        if element_stripped_int < 1 or element_stripped_int > 5:
            print('Sisesta ainult numbreid 1st 5ni.')
            continue
        sisend_array_trimmed_ints.append(element_stripped_int)

    return sisend_array_trimmed_ints


def näita_kasutaja_valikuid_plotil(valikud):
    plot.plot(skp_andmed['Value'],
              label='Sisemajanduse koguprodukt elaniku kohta, eurot')
    teemad = ['jäätmete teke', 'põllumajandus', 'kalapüük', 'f-gaasid']
    sildid = [
        'Jäätmete teke, ' + andmed_dict['jäätmete teke'][1] + ' tuhat tonni',
        'Intensiivpõllumajanduse kasutuses olev maa, ' +
        andmed_dict['põllumajandus'][1] + '% territooriumist',
        'Sisevete kalapüük, ' + andmed_dict['kalapüük'][1] + ' tonni',
        'F-gaaside heitkogus, ' + andmed_dict['f-gaasid'][1] + ' CO2 ekvivalenttonni']
    if 5 in valikud:
        for indeks, teema in enumerate(teemad):
            plot.plot(andmed_dict[teema][0]['Value'], label=sildid[indeks])
    else:
        for valik in valikud:
            plot.plot(andmed_dict[teemad[valik - 1]][0]
                      ['Value'], label=sildid[valik - 1])
    plot.legend()
    plot.show()


def küsi_kasutajalt_sisendit():
    while True:
        kasutaja_input = input(
            'Vali, milliseid näitajaid tahad graafikul SKT-ga võrdlemiseks näha. \n 0 Näita ainult SKT-d \n 1 Jäätmete teke \n 2 Intensiivpõllumajanduse kasutuses olev maa \n 3 Sisevete kalapüük \n 4 F-gaaside heitkogus \n 5 Näita kõiki korraga \n Sisesta näitajate järjekorranumbrid komaga eraldatuna: ')
        if kasutaja_input == '':
            print('\n Sisesta vähemalt üks number!\n')
            continue
        else:
            break
    return kasutaja_input


kasutaja_input = küsi_kasutajalt_sisendit()

kasutaja_valikud = kasutaja_sisend_järjendiks(kasutaja_input)

näita_kasutaja_valikuid_plotil(kasutaja_valikud)
