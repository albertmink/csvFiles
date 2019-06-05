import os
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

print(os.getcwd())

parser = argparse.ArgumentParser(description='plot a given case with two different solutions')

parser.add_argument("--outputfile", help="file to write data", default="test.png",  metavar="output")
parser.add_argument("--csvFile", help="path to csv data", nargs='*')
parser.add_argument("--line", help="path to csv data", default=1, type=int)

args = parser.parse_args()

print(args)

for csv in args.csvFile:
  if( not(os.path.exists(csv)) ):
    print("! file are not available: "+csv )

title=args.outputfile

mu_eff = 4.4

for csv in args.csvFile:
  if( (os.path.exists(csv)) ):
    if( "lena" in csv ) :
      data = np.genfromtxt( csv, delimiter=',', comments='#', dtype=float, usecols=(0,7+args.line) );
      plt.plot(data[:,0],data[:,1], '--', label=str(csv));
    elif( "mink" in csv ):
      data = np.genfromtxt( csv, delimiter=',', comments='#', dtype=float, usecols=(0,1,2,3) );
      plt.plot(data[:,0],data[:,args.line]*4, '--', label=str(csv));
    else :
      data = np.genfromtxt( csv, delimiter=',', comments='#', dtype=float, usecols=(0,1,2,3) );
      plt.plot(data[:,0],data[:,args.line], '--', label=str(csv));

#    plt.plot(data[:,0],7*np.exp(-16*data[:,0])+data[:,1], '+', label=str(csv)+"uncollided");
    #plt.plot(data[:,0], 3*np.exp(-mu_eff*data[:,0]), label="uncollided exp(-"+str(mu_eff)+"*r)")
    #dataLena = np.genfromtxt( "case19_lena.csv", delimiter=',', comments='#', dtype=float );
    #plt.plot(dataLena[:,0],12000000*dataLena[:,1], label='lena 2*10^7')
    print(csv)
    title = "line"+str(args.line)



plt.yscale('log');
#plt.ylim([1e-7,7]);
#plt.xticks(np.arange(0,1,1/mu_eff),np.arange(0,mu_eff));
plt.legend(loc='upper right');
plt.title(title);
plt.savefig(args.outputfile,dpi=240);
print("save figure to "+args.outputfile)
plt.close()
