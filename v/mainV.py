import getXY
import numpy as np
from numpy import linalg as LA

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#print(getXY.getNorm('40case29.csv', 'lena/lena29.csv')[0])
minkv1, lena, err = getXY.getNorm('40case29v1.csv',      '../lena/lena29.csv')
minkv2, lena, err = getXY.getNorm('40case29v2.csv',      '../lena/lena29.csv')
minkv3, lena, err = getXY.getNorm('40case29v3.csv',      '../lena/lena29.csv')
minkv4, lena, err = getXY.getNorm('40case29v4.csv',      '../lena/lena29.csv')
minkv5, lena, err = getXY.getNorm('40case29v5.csv',      '../lena/lena29.csv')
minkv6, lena, err = getXY.getNorm('40case29v6.csv',      '../lena/lena29.csv')
minkv7, lena, err = getXY.getNorm('40case29v7.csv',      '../lena/lena29.csv')
minkv8, lena, err = getXY.getNorm('40case29v8.csv',      '../lena/lena29.csv')
minkv9, lena, err = getXY.getNorm('40case29v9.csv',      '../lena/lena29.csv')
minkv10, lena, err = getXY.getNorm('40case29v10.csv',    '../lena/lena29.csv')
minkv11, lena, err = getXY.getNorm('40case29v11.csv',    '../lena/lena29.csv')
minkv12, lena, err = getXY.getNorm('40case29v12.csv',    '../lena/lena29.csv')
minkv13, lena, err = getXY.getNorm('40case29v13.csv',    '../lena/lena29.csv')
minkN80v8, lena, err = getXY.getNorm('80case29v8.csv',   '../lena/lena29.csv')
minkN80v13, lena, err = getXY.getNorm('80case29v13.csv', '../lena/lena29.csv')



plt.plot(minkv1[:,0],minkv1[:,1],'y.', label='mink40v1')
#plt.plot(minkv1[:,0]-1/30,minkv1[:,1],'y.', label='mink40v1')
#plt.plot(minkv2[:,0],minkv2[:,1],'.', label='mink40v2')
#plt.plot(minkv3[:,0],minkv3[:,1],'.', label='mink40v3')
#plt.plot(minkv4[:,0],minkv4[:,1],'.', label='mink40v4')
#plt.plot(minkv5[:,0],minkv5[:,1],'.', label='mink40v5')
#plt.plot(minkv6[:,0],minkv6[:,1],'.', label='mink40v6')
#plt.plot(minkv7[:,0],minkv7[:,1],'.', label='mink40v7')
plt.plot(minkv8[:,0],minkv8[:,1],'k.', label='mink40v8')
plt.plot(minkN80v8[:,0],minkN80v8[:,1],'k-.', label='mink80v8')
#plt.plot(minkv9[:,0],minkv9[:,1],'.', label='mink40v9')
#plt.plot(minkv10[:,0],minkv10[:,1],'.', label='mink40v10')
#plt.plot(minkv11[:,0],minkv11[:,1],'.', label='mink40v11')
#plt.plot(minkv12[:,0],minkv12[:,1],'.', label='mink40v12')
plt.plot(minkv13[:,0],minkv13[:,1],'g.', label='mink40v13')
plt.plot(minkN80v13[:,0],minkN80v13[:,1],'g-.', label='mink80v13')
#mink100, lena100, err100 = getXY.getNorm('minkTauEins/100case29.csv', 'lena/lena29.csv')
#plt.plot(mink100[:,0], mink100[:,1],'.', label='mink100D1')
plt.plot(lena[:,0], lena[:,1], 'r--', label='lena')
plt.yscale('log');
plt.ylim([1e-4,10]);
plt.legend(loc='upper right');
plt.savefig('scaling_omega_sink.png',dpi=240);

exit(-1)
