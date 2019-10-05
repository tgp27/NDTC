#!/usr/bin/env python
# coding: utf-8

# # Gorgeous matplotlib plot
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig

# In[89]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,200)
y1 = np.sin(x)
y2 = np.cos(x)

# create a blank set of axes, with background colour (R,G,B)
# default bground colour is white
ax = plt.axes(facecolor=(0.9, 0.9, 0.9))

ax.plot(x,y1,label='sine',linewidth=2, alpha=0.5, c=(0.0, 0.0, 0.0))
ax.plot(x,y2,label='cosine',linewidth=2, alpha=0.5, c=(0.0, 1.0, 0.0))

plt.xlim((0.0,10.0))
plt.ylim((-1.5,1.5))

# end point has to go one further than what you really want (convention)
plt.xticks(np.arange(0, 11, step=1))

#plt.text(1.0, 50.0, r'$y(x) = (x-2)(x-5)(x-8)$', fontsize=12)

# add x label, with some design choices, r is for red
ax.set_xlabel('Time (s)',color='k',fontsize=14,family='Verdana', labelpad=10)
# add y label with extra padding (push it more to the left)
ax.set_ylabel('Amplitude (arb. units)',color='k',fontsize=14,family='Verdana', labelpad=10)

# add a plot title
plt.title('trigonometric functions', loc='left', fontsize=16, family='Verdana', y=1.03)

#plt.arrow(2.0,-0.3,0.9,0.3, linestyle=':', linewidth='2.0', head_width=0.3, head_length=0.3, fc='w', ec='r')

# add legend to the plot, location loc=1 (integer) means top right (don't ask me why)
# more info on loc from the link above
# alpha is transparency of frame box
# you have to write edgecolor not ec for plt.legend, unlike plt.arrow (above)
# borderpad adds some space around the legend text
plt.legend(bbox_to_anchor=(0.57,0.30), prop={'size': 12}, fontsize='large', framealpha = 0.8, edgecolor = None,borderpad=0.3)
plt.savefig('gorge_plot.pdf', dpi=96, bbox_inches='tight', pad_inches=0.2)
plt.show()


# In[ ]:




