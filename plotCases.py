import getXY
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

path = 'finiteBeam/'
line = 1

for i in range(1,36):
    dfMacro = pd.DataFrame(index=np.linspace(0,1,101))
    dfMacro['macro50*4'] = pd.Series(getXY.getDataMink(path+'mink/50case'+str(i)+'.csv', line)[:,1]*5, index=dfMacro.index)
    dfMacro['meso100'] = pd.Series( getXY.getDataMcHardy(path+'mcHardyRK/100case'+str(i)+'.csv', line)[:,1], index=dfMacro.index )
    dfMacro['MC'] = pd.Series(getXY.getDataLena(path+'lena/lena'+str(i)+'.csv', line)[:,1], index=dfMacro.index)
    dfMacro.plot()
    plt.yscale('log')
    plt.title('case'+str(i))
    plt.savefig(path+'compare_'+str(line)+"_case"+str(i)+'.png')
    plt.close()
