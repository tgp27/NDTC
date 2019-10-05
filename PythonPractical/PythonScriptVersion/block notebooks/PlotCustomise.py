#!/usr/bin/env python
# coding: utf-8

# # Customisation of matplotlib plots
# 
# Below is a (very ugly) example plot of three functions using matplotlib.
# 
# I have included the most common alterations you will want to make to your plots.
# 
# ## Sources
# * [pyplot documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html)
# * [a full guide to the color variable, with examples](https://matplotlib.org/gallery/color/color_demo.html#sphx-glr-gallery-color-color-demo-py)
# * [plt.legend documentation](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend). Includes more info on the location (loc) convention
# * [more info on fonts](https://matplotlib.org/gallery/api/font_family_rc_sgskip.html)
# 
# * [more info on arrows](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.arrow.html)
# 
# * [fancy arrows](https://matplotlib.org/gallery/pyplots/whats_new_98_4_fancy.html#sphx-glr-gallery-pyplots-whats-new-98-4-fancy-py)
# 

# In[184]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
# define the x axes (from -10 to 10 in 200 linearly spaced points)
x = np.linspace(-10,10,200)
# three random functions I picked to plot
y1 = (1-np.cos(x))/x
y2 = -np.tanh(x)
y3 = np.sqrt(np.abs(x)+1)

# create a blank set of axes, with background colour (R,G,B)
# default bground colour is white
ax = plt.axes(facecolor=(0.9, 0.9, 0.5))

#
# add a plot to the axes object ax
# alpha is the transparency of the line (float from 0.0 to 1.0)
# c is for color. accepts common colour names (e.g. green, yellow)
ax.plot(x,y1,label='Ylabel1',linewidth=7.1,alpha=0.5, c='blue')

# another way to plot, using plt.plot instead of ax.plot. 
# They're equivalent if you've already created axes.
plt.plot(x,y2,label='Ylabel2',linewidth=3.0,color='green')

# a third way to plot: by defining a Line instance
# k for key = black
# 'k--' means plot a black dashed line
# note use of double quotes so i could include the apostrophe in "won't"
line, = plt.plot(x,y3,'k--',label= "You won't see this label anyway")
     
# another way to label lines, or re-setting the label of a line after creating it
line.set_label('Boo')

# define the x axis limits (y axis can be set similarly)
plt.xlim((-2.5,4.0))

# choose custom tick marks: from -2.4 to 3.2 in steps of 0.4
plt.xticks(np.arange(-2.4, 3.2, step=0.4))

# Add floating text to the plot at a given (x,y) location. 
# Can include LaTeX-type maths expressions
plt.text(-1.6, 2.0, r'Some text and maths, $\mu^2=\sqrt{100}$')

# add x label, with some design choices, r is for red
ax.set_xlabel('Some x label',color='r',fontsize=16,family='Tahoma')
# add y label with extra padding (push it more to the left)
ax.set_ylabel('And y label', labelpad=50)

# add a plot title
plt.title('The title',fontsize=18,family='Times New Roman' )


# add an arrow with origin at (2.0,-0.3) and x,y length (0.9,0.3)
# fc = facecolor (fill)
# ec = edgecolor
plt.arrow(2.0,-0.3,0.9,0.3, linestyle=':', linewidth='2.0', head_width=0.3, head_length=0.3, fc='w', ec='r')

# add legend to the plot, location loc=1 (integer) means top right (don't ask me why)
# more info on loc from the link above
# alpha is transparency of frame box
# you have to write edgecolor not ec for plt.legend, unlike plt.arrow (above)
# borderpad adds some space around the legend text
plt.legend(loc=1, fontsize='large', framealpha = 0.8, edgecolor = 'red',borderpad=1)
plt.show()


# ## Suggested further actions
# 
# * choose a plot style you like and save it as a template for future use
# * if you're plotting the same thing over and over, make a module/function you can call which plots the data and saves the plot as a .png or .pdf file to a given location

# In[ ]:




