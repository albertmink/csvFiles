import getXY
import numpy as np
from numpy import linalg as LA

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


'get me all norm gerichted'
absErrMcHardy = []
absErrMcHardyRel = []
absErrMink = []
absErrMinkRel = []
absErrMinkT1 = []
absErrMinkRelT1 = []
for i in range(1,36):
    absErrMinkT1.append(getXY.getNorm('minkTauEins/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    absErrMinkRelT1.append(getXY.getNormRel('minkTauEins/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    absErrMink.append(getXY.getNorm('mink/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    absErrMinkRel.append(getXY.getNormRel('mink/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    absErrMcHardy.append(getXY.getNorm('mcHardyRK/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    absErrMcHardyRel.append(getXY.getNormRel('mcHardyRK/100case'+str(i)+'.csv', 'lena/lena'+str(i)+'.csv' ))
    dataMinkT1 = getXY.getDataMink('minkTauEins/100case'+str(i)+'.csv')
    plt.plot(dataMinkT1[:,0],dataMinkT1[:,1], 'c-', label='macro tau=1')
    dataMink = getXY.getDataMink('mink/100case'+str(i)+'.csv')
    plt.plot(dataMink[:,0],dataMink[:,1], 'm-', label='macro')
    dataLena = getXY.getDataLena('lena/lena'+str(i)+'.csv')
    plt.plot(dataLena[:,0], dataLena[:,1], 'y-', label='MC')
    plt.legend()
    plt.yscale('log');
    plt.savefig('plots/macroMC'+str(i)+'.png')
    plt.close()
    dataMcHardy = getXY.getDataMcHardy('mcHardyRK/100case'+str(i)+'.csv')
    plt.plot(dataMcHardy[:,0],dataMcHardy[:,1], 'g-', label='meso')
    plt.plot(dataLena[:,0], dataLena[:,1], 'y-', label='MC')
    plt.legend()
    plt.yscale('log');
    plt.savefig('plots/mesoMC'+str(i)+'.png')
    plt.close()

#print(absErrMink)
#print(absErrMinkRel)

plt.yscale('log');
#plt.ylim([10e-4,10]);
plt.plot(absErrMinkT1, 'c--', label='minkT1');
plt.plot(absErrMinkRelT1, 'c.', label='minkRelT1');
plt.plot(absErrMink, 'm--', label='mink');
plt.plot(absErrMinkRel, 'm.', label='minkRel');
plt.plot(absErrMcHardy, 'g--', label='mcHardy');
plt.plot(absErrMcHardyRel, 'g.', label='mcHardyRel');
plt.legend(loc='center left');
plt.savefig('absErrMink.png',dpi=240);
plt.close()
