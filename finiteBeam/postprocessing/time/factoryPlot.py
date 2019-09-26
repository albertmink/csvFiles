from shutil import copyfile

import numpy as np
import pandas as pd

timeCPU = list()
iterations = list()
cases = list()
for a in range(1,6):
  for b in [0,5,10,15,20,25,30]:
    i = a+b
    cases.append(i)
    #fin = open("./job.2645_"+str(i)+".out", 'rt') #mink 50er data
    #fin = open("./job.2597_"+str(i)+".out", 'rt') #mink 100er data
    fin = open("./job.2562_"+str(i)+".out", 'rt') #mcHardyRK 100er data
    data = fin.readlines()
    # get iteration
    for line in data:
      if 'converged' in line:
        it = [int(i) for i in line.split() if i.isdigit()]
        iterations.append(it[0])
        break
  
    # get time
    for line in data:
      if 'time (cpu)' in line:
        splitLine = line.split()
        timeInSec = int(float(splitLine[4][:-1]))
        timeCPU.append(timeInSec)
        break

df = pd.DataFrame(np.array([timeCPU,iterations]).transpose(), index=cases, columns=['sec','it'])
df.to_csv('./job.2562.csv',index_label='case')
