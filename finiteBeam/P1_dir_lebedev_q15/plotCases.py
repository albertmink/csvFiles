import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



line = 1

def getDataValues( caseFile, line=1 ):
    df = pd.read_csv(caseFile, index_col=0, header=None)[line]
    return df.values

for i in range(1,36):
    dfMacro = pd.DataFrame(index=np.arange(0,0.99,0.01))
    dfMacro['p1_q15_lebedev'] = getDataValues('100case'+str(i)+'.csv', line)[:-2]
#    dfMacro['meso_q7_N100'] = getDataValues('../mcHardyRK_d3q7/100case'+str(i)+'.csv', line)[:-2]
    dfMacro['MC'] = getDataValues('../lena/lena'+str(i)+'.csv', line)[:-2]
    dfMacro.plot()
    plt.yscale('log')
    plt.savefig('./case'+str(i)+'.png')
    plt.close()
