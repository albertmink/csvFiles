import pandas as pd

df = pd.read_csv('err_finiteBeam.csv', index_col=0)

print(df)

l = (0.1,0.4,0.7,0.9,1.0)

df1 = df.loc[df.index%5 == 1]
df2 = df.loc[df.index%5 == 2]
df3 = df.loc[df.index%5 == 3]
df4 = df.loc[df.index%5 == 4]
df5 = df.loc[df.index%5 == 0]

df1.to_csv('finiteAlbedo01.csv', float_format='%8.6e')
df2.to_csv('finiteAlbedo04.csv', float_format='%8.6e')
df3.to_csv('finiteAlbedo07.csv', float_format='%8.6e')
df4.to_csv('finiteAlbedo09.csv', float_format='%8.6e')
df5.to_csv('finiteAlbedo10.csv', float_format='%8.6e')
