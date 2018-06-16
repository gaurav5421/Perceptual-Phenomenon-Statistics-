import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#data = pd.read_csv(‘C:\Users\gsureka\Google Drive\Udacity\Project_1\stroopdata.csv')

data = pd.read_csv('/Users/gauravsureka/Google Drive/Udacity/Project_1/stroopdata.csv')
Incongruent  = data['Incongruent']
Congruent = data['Congruent']

data1 = [Incongruent,Congruent]

fig = plt.figure()
ax = fig.add_subplot(111)
bp = ax.boxplot(data1)
ax.set_xticklabels(['Incongruent','Congruent'])
# plt.boxplot(data1)
# plt.set_xticklabels(['Incongruent','Congruent'])
fig.savefig('Comparison.png')

397k5oOTUK2vzGkCnEoI