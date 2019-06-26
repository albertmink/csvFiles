import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import getXY
from colorspacious import cspace_converter

cmap = matplotlib.cm.get_cmap('Accent')


caseNb = 0
for alb in range(1,6):
  for opticDepth in range(1,8):
    caseNb += 1
    caseMink = ("../mink/50case"+str(caseNb)+".csv")
    caseMcHardy = ("../mcHardyRK/100case"+str(caseNb)+".csv")
    caseLena = ("../lena/lena"+str(caseNb)+".csv")
    plt.plot(getXY.getDataLena(caseLena)[:,0],getXY.getDataLena(caseLena)[:,1], '--',color=cmap(opticDepth-1), label=str(caseNb));
    plt.plot(getXY.getDataMink(caseMink)[:,0],getXY.getDataMink(caseMink)[:,1]*4, 'x', color=cmap(opticDepth-1), label=str(caseNb));
    plt.plot(getXY.getDataMink(caseMcHardy)[:,0],getXY.getDataMcHardy(caseMcHardy)[:,1], '^', color=cmap(opticDepth-1), label=str(caseNb));
  plt.yscale('log');
  plt.savefig('albedo'+str(caseNb)+".png")
  plt.close()
