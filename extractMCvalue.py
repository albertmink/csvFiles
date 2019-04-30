import getXY
import numpy as np
import pandas as pd


df = pd.read_csv('caseDefinition.csv',index_col=0)

# task:
# get MC simulation data at distance mfp

for i in range(1,36):
    mfp = df.loc[i].mfp
    dataLena = getXY.getDataLena('lena/lena'+str(i)+'.csv')
    indexInDataLena = int(mfp*100)
    print(dataLena[indexInDataLena,1])
