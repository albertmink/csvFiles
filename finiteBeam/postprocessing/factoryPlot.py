from shutil import copyfile

import numpy as np
import pandas as pd

def getDataValues( caseFile, line=1 ):
    df = pd.read_csv(caseFile, index_col=0, header=None)[line]
    return df.values

line = 3
for i in range(1,36):
  ymin = min(getDataValues('../lena/lena'+str(i)+'.csv', line))/10
  #ymin=1e-13, ymax=10,
  print(ymin)
  copyfile("case1_template.tex","case"+str(i)+".tex")
  fin = open("case"+str(i)+".tex", 'rt')
  data = fin.read()
  data = data.replace('26.csv',str(i)+'.csv')
  data = data.replace(str(1e-13),str(ymin))
  fin.close()
  fout = open("case"+str(i)+".tex", 'wt')
  fout.write(data)
  fout.close()

