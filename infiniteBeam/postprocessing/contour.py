import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfErr =pd.read_csv("err_infiniteBeam.csv", index_col='case')
dfCase =pd.read_csv("caseDefinition.csv", index_col='case')

x = dfCase["mu_t"].unique()
y = dfCase["albedo"].unique()

X,Y = np.meshgrid(x,y)
print(X)
print(Y)

ma = dfErr["absMa1Normalized"].values.reshape(x.size, y.size)
me = dfErr["absMe1Normalized"].values.reshape(x.size, y.size)
print(ma)


fig, ax = plt.subplots()
CS = ax.contour(X, Y, np.transpose(ma))
ax.clabel(CS, inline=1, fontsize=10)
#plt.show()
plt.xlabel("Optical depth")
plt.ylabel("Scattering albedo")
plt.savefig("ma1normalized.png")
plt.close()

fig, ax = plt.subplots()
CS = ax.contour(X, Y, np.transpose(me))
ax.clabel(CS, inline=1, fontsize=10)
#plt.show()
plt.xlabel("Optical depth")
plt.ylabel("Scattering albedo")
plt.savefig("me1normalized.png")
plt.close()
