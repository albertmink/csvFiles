import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


## call from terminal for all 35 cases:
# for i in {1..35}; do python3 gerichted.py --caseNb ${i}; done;
#


parser = argparse.ArgumentParser(description='plot a given case with two different solutions')
parser.add_argument("--caseNb", help="provide case number", type=int)
args = parser.parse_args()


# path to csv are static
mink 		= 'minkTauEins/100case'+str(args.caseNb)+'.csv'
mcHardy = 'mcHardyRK/100case'+str(args.caseNb)+'.csv'
lena 		= 'lena/lena'+str(args.caseNb)+'.csv'

dataMink = np.genfromtxt( mink, delimiter=',', comments='#', dtype=float, usecols=(0,1) );
plt.plot(dataMink[:,0],dataMink[:,1], '--', label=str(args.caseNb)+'mink');

dataMcHardy = np.genfromtxt( mcHardy, delimiter=',', comments='#', dtype=float, usecols=(0,1), skip_header=1 );
plt.plot(dataMcHardy[:,0],dataMcHardy[:,1], '--', label=str(args.caseNb)+'mcHardy');

dataLena = np.genfromtxt( lena, delimiter=',', comments='#', dtype=float, usecols=(0,8) );
plt.plot(dataLena[:,0],dataLena[:,1], '--', label=str(args.caseNb)+'lena');



plt.yscale('log');
#plt.ylim([10e-15,7]);
plt.legend(loc='upper right');
plt.savefig("plots/gerichtet"+str(args.caseNb)+".png",dpi=240);
plt.close()
