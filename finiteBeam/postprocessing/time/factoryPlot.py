from shutil import copyfile

import numpy as np
import pandas as pd

dfCase = pd.read_csv('../../../caseDefinition.csv')

timeCPU = list()
iterations = list()
cases = list()
opticalDepth = list()
albedo = list()
for a in range(1,6):
  for b in [0,5,10,15,20,25,30]:
    i = a+b
    opticalDepth.append(dfCase['mu_t'][i-1])
    albedo.append(dfCase['albedo'][i-1])
    cases.append(i)
#    opticalDepth.append(i)
#    albedo.append(dfCase['albedo'][i])
    #fin = open("./job.2645_"+str(i)+".out", 'rt') #mink 50er data
    #fin = open("./job.2597_"+str(i)+".out", 'rt') #mink 100er data
#    fin = open("./job.2562_"+str(i)+".out", 'rt') #mcHardyRK 100er data
    fin = open("./../../mcHardy160/job.3025_"+str(i)+".out", 'rt') #mcHardyRK 160er data
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

df = pd.DataFrame(np.array([timeCPU,iterations,opticalDepth,albedo]).transpose(), index=cases, columns=['sec','it','opticalDepth','albedo'])
df2 = pd.DataFrame({"sec":[99], "it":[99], "opticalDepth":[99], "albedo":[1.9]}, index=[99])
df = df.append(df2,sort=False)
df.to_csv('./mcHardy160.csv',index_label='case')
