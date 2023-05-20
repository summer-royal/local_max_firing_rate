%%time

#looped version that is more aesthetically-pleasing
#created just for fun

import numpy as np
import random
import matplotlib.pyplot as plt

#Loading up the data—run this cell
rates = np.loadtxt('rates.txt')

#create empty array to store local max data
local_max = [None]*100000

#loop through the rates at each time 
#compare the magnitude of the current rate to the previous and next rate
#if the current rate is a local max, save it in local_max
for i in range (rates.size - 1):
  if (i > 0):
    if ((rates[i] > rates[i-1]) and (rates[i] > rates[i+1])):
      local_max[i] = rates[i]

#the following code creates a plot of the firing rate
# and includes the extracted times as a subplot on the same graph
fig, rates_data = plt.subplots()

rates_X = np.arange(0, 1000, 1)
rates_Y = rates[0:1000]

color = 'tab:red'
rates_data.set_xlabel('Time')
rates_data.set_ylabel('Rate')
rates_data.plot(rates_X, rates_Y, color=color)


local_max_X = np.arange(0, 1000, 1)
local_max_Y = local_max[0:1000]

color = 'tab:blue'
plt.scatter(local_max_X, local_max_Y, color=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
