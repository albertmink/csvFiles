import numpy as np
import pandas as pd

df = pd.read_csv('./mink160.csv')
df = df.sort_values(by='case')
# dummy to append
dfDummy = pd.DataFrame({"case":[99], "sec":[99], "it":[99], "opticalDepth":[99], "albedo":[1.9]})

df1 = df[0:  5]
df2 = df[5: 10]
df3 = df[10:15]
df4 = df[15:20]
df5 = df[20:25]
df6 = df[25:30]
df7 = df[30:35]

df1 = df1.append(dfDummy)
df2 = df2.append(dfDummy)
df3 = df3.append(dfDummy)
df4 = df4.append(dfDummy)
df5 = df5.append(dfDummy)
df6 = df6.append(dfDummy)
df7 = df7.append(dfDummy)

df1.to_csv('./mink160_2.csv',index=False)
df2.to_csv('./mink160_4.csv',index=False)
df3.to_csv('./mink160_6.csv',index=False)
df4.to_csv('./mink160_8.csv',index=False)
df5.to_csv('./mink160_12.csv',index=False)
df6.to_csv('./mink160_20.csv',index=False)
df7.to_csv('./mink160_30.csv',index=False)
