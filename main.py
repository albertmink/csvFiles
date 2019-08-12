import getXY
import numpy as np
from numpy import linalg as LA
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


erMacro = pd.DataFrame(index=np.arange(1,36))
erMeso = pd.DataFrame(index=np.arange(1,36))

dfCase = pd.read_csv('caseDefinition.csv',index_col=0)
energy1 = []
energy2 = []
energy3 = []

setUp = 'infiniteBeam/'

for i in range(1,36):
    mfp = dfCase.loc[i].mfp
    indexAwayFromBoundary = 2
    # mask boundary region about a mfp
    #indexAwayFromBoundary = int(round(mfp,2)*100) *1
    #print(indexAwayFromBoundary)
    dataLena1 = getXY.getDataLena(setUp+'lena/lena'+str(i)+'.csv', 1)
    dataLena2 = getXY.getDataLena(setUp+'lena/lena'+str(i)+'.csv', 2)
    dataLena3 = getXY.getDataLena(setUp+'lena/lena'+str(i)+'.csv', 3)
    # macro 
    erMacro.at[i,'absMa1'] = getXY.getNorm4(setUp+'mink/50case'+str(i)+'.csv', dataLena1, 1, indexAwayFromBoundary)
    erMacro.at[i,'absMa2'] = getXY.getNorm4(setUp+'mink/50case'+str(i)+'.csv', dataLena2, 2, indexAwayFromBoundary)
    erMacro.at[i,'absMa3'] = getXY.getNorm4(setUp+'mink/50case'+str(i)+'.csv', dataLena3, 3, indexAwayFromBoundary)

    # meso
    erMeso.at[i,'absMe1'] = getXY.getNorm(setUp+'mcHardyRK/100case'+str(i)+'.csv', dataLena1, 1, indexAwayFromBoundary)
    erMeso.at[i,'absMe2'] = getXY.getNorm(setUp+'mcHardyRK/100case'+str(i)+'.csv', dataLena2, 2, indexAwayFromBoundary)
    erMeso.at[i,'absMe3'] = getXY.getNorm(setUp+'mcHardyRK/100case'+str(i)+'.csv', dataLena3, 3, indexAwayFromBoundary)

    energy1.append(getXY.getTotalEnergy(setUp+'lena/lena'+str(i)+'.csv', 1, indexAwayFromBoundary))
    energy2.append(getXY.getTotalEnergy(setUp+'lena/lena'+str(i)+'.csv', 2, indexAwayFromBoundary))
    energy3.append(getXY.getTotalEnergy(setUp+'lena/lena'+str(i)+'.csv', 3, indexAwayFromBoundary))


tmp = erMacro.join(erMeso)
tmp['totalEnergy1'] = energy1
tmp['totalEnergy2'] = energy2
tmp['totalEnergy3'] = energy3
tmp['absMa1Normalized'] = tmp['absMa1']/tmp['totalEnergy1']
tmp['absMe1Normalized'] = tmp['absMe1']/tmp['totalEnergy1']
tmp['absMa2Normalized'] = tmp['absMa2']/tmp['totalEnergy2']
tmp['absMe2Normalized'] = tmp['absMe2']/tmp['totalEnergy2']
tmp['absMa3Normalized'] = tmp['absMa3']/tmp['totalEnergy3']
tmp['absMe3Normalized'] = tmp['absMe3']/tmp['totalEnergy3']

tmp.index.names = ['case']

tmp.insert(loc=0,column='mu_t',value=dfCase['mu_t'].values)

print(tmp[['absMa1', 'absMa1Normalized', 'absMe1', 'absMe1Normalized']])
tmp.to_csv('err_'+setUp[:-1]+'.csv', float_format='%8.6e')

#tmp[['absMa1Normalized','absMe1Normalized']].plot()
#plt.yscale('log');
#plt.savefig('errorNormalized.png',dpi=240);
#plt.close()
