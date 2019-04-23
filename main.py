import getXY
import numpy as np
from numpy import linalg as LA

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


'get me all norm gerichted'
absErrMcHardy = []
absErrMink = []
for i in range(1,36):
    print("case"+str(i))
    absErrMink.append(getXY.getNorm('minkTauEins/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    absErrMcHardy.append(getXY.getNorm('mcHardyRK/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    dataMink = getXY.getDataMink('minkTauEins/100case'+str(i)+'.csv')
    plt.plot(dataMink[:,0],dataMink[:,1])
    dataLena = getXY.getDataLena('lena/lena'+str(i)+'.csv')
    plt.plot(dataLena[:,0], dataLena[:,1])
    plt.yscale('log');
    plt.savefig('plots/macroMC'+str(i)+'.png')
    plt.close()


plt.yscale('log');
#plt.ylim([10e-4,10]);
plt.plot(absErrMink, '--', label='mink');
plt.plot(absErrMcHardy, '--', label='mcHardy');
plt.legend(loc='upper right');
plt.savefig('absErrMink.png',dpi=240);
plt.close()
