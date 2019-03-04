import pandas as pd
import matplotlib.pyplot as plot
from sisevete_kalapüük import *

põllumajandusmaa_andmed = bioloogilise_mitmekesisuse_vahenemine.ix[bioloogilise_mitmekesisuse_vahenemine['Näitaja'] ==
                                                                   'Intensiivpõllumajanduse kasutuses olev maa, % territooriumist']

põllumajandusmaa_andmed.pop('Näitaja')

põllumajandusmaa_andmed['Value'] = korruta_tulba_väärtused(
    põllumajandusmaa_andmed['Value'], 2500)

print(põllumajandusmaa_andmed)
