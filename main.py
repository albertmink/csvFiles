import getXY
import numpy as np
from numpy import linalg as LA
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


'get me all norm gerichted'
absErrMcHardy = []
absErrMcHardyRel = []
absErrMinkN50 = []
absErrMinkRelN50 = []
absErrMink = []
absErrMinkRel = []
absErrMinkT1 = []
absErrMinkRelT1 = []

dfMacro = pd.DataFrame(index=np.linspace(0,1,101))
dfMeso = pd.DataFrame(index=np.linspace(0,1,101))
erMacro = pd.DataFrame(index=np.arange(1,36))
erMeso = pd.DataFrame(index=np.arange(1,36))



for i in range(1,36):
    # macro 
    erMacro.at[i,'abs50'] = getXY.getNorm('mink/50case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    erMacro.at[i,'abs100'] = getXY.getNorm('mink/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    erMacro.at[i,'rel50'] = getXY.getNormRel('mink/50case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    erMacro.at[i,'rel100'] = getXY.getNormRel('mink/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    erMacro.at[i,'absT1_100'] = getXY.getNorm('minkTauEins/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    erMacro.at[i,'relT1_100'] = getXY.getNormRel('minkTauEins/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    dfMacro['50'] = pd.Series(getXY.getDataMink('mink/50case'+str(i)+'.csv')[:,1], index=dfMacro.index)
    dfMacro['100'] = pd.Series(getXY.getDataMink('mink/100case'+str(i)+'.csv')[:,1], index=dfMacro.index)
    #dfMacro['150'] = pd.Series(getXY.getDataMink('mink/150case'+str(i)+'.csv')[:,1], index=dfMacro.index)
    dfMacro['MC'] = pd.Series(getXY.getDataLena('lena/lena'+str(i)+'.csv')[:,1], index=dfMacro.index)
    #plot single cases
    dfMacro.plot()
    plt.yscale('log')
    plt.savefig('plots/macroMC'+str(i)+'.png')
    plt.close()
    # meso
    erMeso.at[i,'absMeso'] = getXY.getNorm('mcHardyRK/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    erMeso.at[i,'relMeso'] = getXY.getNormRel('mcHardyRK/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' )
    #plot single cases
    dfMeso['100'] = pd.Series(getXY.getDataMcHardy('mcHardyRK/100case'+str(i)+'.csv')[:,1], index=dfMacro.index)
    dfMeso.plot()
    plt.yscale('log')
    plt.savefig('plots/mesoMC'+str(i)+'.png')
    plt.close()


tmp = erMacro.join(erMeso)
print(tmp)
tmp.plot()
plt.yscale('log');
plt.savefig('absErrMink.png',dpi=240);
plt.close()
