#!/usr/bin/env python
# coding: utf-8

# # Simple histogram

# ### Create a histogram of a 1D array of float values

# First, import necessary packages. numpy for handling arrays and pyplot from matplotlib for making the histogram.

# In[2]:


import numpy as np 
import matplotlib.pyplot as plt


# We will generate some random data to plot in the histogram: a normal distribution with mean 10.0 and SD 3.0 (for more info see the RandomValues block). 2000 values in total. The first 10 values are displayed as an example.

# In[3]:


rng = np.random.RandomState(727)  # deterministic random data
array = rng.normal(loc=10.0, scale = 3.0, size=2000)
print(array[0:10])


# Create a histogram using the given data. 
# 
# The inputs are
# - "array", the 1D array we created above
# - "bins", the number of bins (aka buckets) into which the data are divided. The bin size is automatically chosen in this example (bins='auto'), but you could manually select the number of bins (any positive integer).
# - "color", the colour of the histogram bars (note American English spelling of colour). I've chosen a nice shade of blue.
# - "ec", edge colour, colour of the edge around the histogram bars
# - "lw", linewidth, thickness of the edge around the histogram bars
#    
# 
# 
# More info on the hist function here: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html

# In[4]:


n, bins, patches = plt.hist(array, bins='auto', color = "red", ec="black", lw=2)
plt.show()


# The outputs are
# - the histogram itself (the plt.hist object, not an explicit output)
# - "n", the number of counts for each bin (a 1D array of values which add up to 2000)
# - "bins", the number of bins
# - The "patches" output requires a little more explanation. The plt module creates the figure of the histogram by making a blank 2D plot and then adding rectangular "patches", one for each bin of the histogram. The "patches" output is just the set of these rectangles. You will probably never need to worry about this, but I thought you'd like to know anyway.
# 

# The plot displays a histogram matching the normal distribution we expected.
# 
# ## Things to play with:
# ### Basic
# - change the random number seed value to get a different random distribution.
# - change the parameters of the data distribution (mean and standard deviation)
# - change the type of distribution (something other than normal)
# - check that the total number of counts adds up to 2000 (using the array "n")
# - change the number of bins
# 
# ### Advanced (requires additional research)
# - plot two distributions on the same histogram (array1, array2).
# - manually choose the axis limits (e.g. choose x axis from 0.0 to 20.0)
# - changing axes font size and type

# In[ ]:




