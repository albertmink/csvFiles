import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

path = './finiteBeam/'

# scaling for diffuse mode
## finiteBeam
#  * factor 4
## finiteBeamDiffuse
#  * factor 3
## infiniteBeam
#  * factor 5
## infiniteBeamDiffuse
#  * factor 4


line = 1

def getDataValues( caseFile, line=1 ):
    df = pd.read_csv(caseFile, index_col=0, header=None)[line]
    return df.values

for i in range(1,36):
    dfMacro = pd.DataFrame(index=np.arange(0,0.99,0.01))
    dfMacro['meso_q15_N50'] = getDataValues(path+'mcHardyRK_d3q15/50case'+str(i)+'.csv', line)[:-2]
    dfMacro['meso_q15_N100'] = getDataValues(path+'mcHardyRK_d3q15/100case'+str(i)+'.csv', line)[:-2]
    #dfMacro['meso_q7_N100'] = getDataValues(path+'mcHardyRK_d3q7/100case'+str(i)+'.csv', line)[:-2]
    dfMacro['meso_q15_N150'] = getDataValues(path+'mcHardyRK_d3q15/150case'+str(i)+'.csv', line)[:-2]
    #dfMacro['meso_q15_N100'] = getDataValues(path+'mcHardyRK_d3q15/100case'+str(i)+'.csv', line)[:-2]
    #dfMacro['meso_q27_N100'] = getDataValues(path+'mcHardyRK/100case'+str(i)+'.csv', line)[:-2]
    dfMacro['MC'] = getDataValues(path+'lena/lena'+str(i)+'.csv', line)[:-2]
    dfMacro.plot()
    plt.yscale('log')
    plt.title('case'+str(i))
    plt.savefig(path+'meso_d3q15_grid_'+str(line)+"_case"+str(i)+'.png')
    plt.close()
