import pandas as pd

for case in range(1,36):
  filename = "lena"+str(case)+".csv"
  df=pd.read_csv(filename,header=None)
  df[[0,8,10,12]].to_csv(filename, index=None, header=None)
