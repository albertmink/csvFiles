import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib2tikz import save as tikz_save
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

mesoDF = pd.read_csv('./job.2562.csv')
macroDF = pd.read_csv('./job.2597.csv')


fig, ax = plt.subplots()
#labels = ['0.1, 0.4, 0.7, 0.9, 1']
#xLabels = ['2,4,8,12,20,30']
#xLabels = np.arange(1,36).tolist()
#x = np.arange(len(xLabels))
width = 0.18
barWidth = 0.08

#dataMeso = mesoDF.sort_values(by=['case'])
dataMeso = (mesoDF['sec'].tolist())
dataMacro = macroDF['sec'].tolist()

xLabels = ['b=2', 'b=4', 'b=6', 'b=8', 'b=12', 'b=20', 'b=30']
x = np.arange(len(xLabels))

print(dataMeso[0:7])
print(dataMeso[7:14])
print(dataMeso[14:21])
print(dataMeso[21:28])
print(dataMeso[28:35])
ax.bar(x-2*width, dataMeso[0:7],   barWidth, label='a=0.1', color='gold'      , hatch='-'*3)
ax.bar(x-1*width, dataMeso[7:14],  barWidth, label='a=0.4', color='limegreen' , hatch='-'*3)
ax.bar(x+0*width, dataMeso[14:21], barWidth, label='a=0.7', color='royalblue' , hatch='-'*3)
ax.bar(x+1*width, dataMeso[21:28], barWidth, label='a=0.9', color='firebrick' , hatch='-'*3)
ax.bar(x+2*width, dataMeso[28:35], barWidth, label='a=1.0', color='blueviolet', hatch='-'*3)

ax.bar(x-2*width+barWidth, dataMacro[0:7],   barWidth, label='a=0.1', color='gold'      , hatch='/'*3)
ax.bar(x-1*width+barWidth, dataMacro[7:14],  barWidth, label='a=0.4', color='limegreen' , hatch='/'*3)
ax.bar(x+0*width+barWidth, dataMacro[14:21], barWidth, label='a=0.7', color='royalblue' , hatch='/'*3)
ax.bar(x+1*width+barWidth, dataMacro[21:28], barWidth, label='a=0.9', color='firebrick' , hatch='/'*3)
ax.bar(x+2*width+barWidth, dataMacro[28:35], barWidth, label='a=1.0', color='blueviolet', hatch='/'*3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Seconds')
ax.set_xticks(x)
ax.set_ylim((0,4000))
ax.set_xticklabels(xLabels)
custom_lines = [Line2D([0],[0], color='gold', lw=4),
Line2D([0],[0], color='limegreen', lw=4),
Line2D([0],[0], color='royalblue', lw=4),
Line2D([0],[0], color='firebrick', lw=4),
Line2D([0],[0], color='blueviolet',lw=4),
Patch(facecolor='white', hatch='-'*3),
Patch(facecolor='white', hatch='/'*4)
]

ax.legend(custom_lines, ['a=0.1','a=0.4','a=0.7', 'a=0.9', 'a=1', 'meso RTLBM', 'macro RTLBM'])

fig.tight_layout()

tikz_save('mytikz.tex')
plt.show()
plt.savefig('timeCompHatch.pdf')
