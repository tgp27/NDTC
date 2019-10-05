#!/usr/bin/env python
# coding: utf-8

# Problem: Define a function that accepts a 1D array $x$ as input and produces a normally-distributed array of values $y$ as output:
# 
# $$ y = f(x,\mu,\sigma) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
# 
# Solution:

# In[ ]:


def norm_dist(in_arr, mean, sd):
    out_arr = (sd*np.sqrt(2*np.pi))**(-1)*np.exp(-(in_arr - mean)**2/(2*sd**2))
    return out_arr


# We check it works by applying it to some values and plotting the output:

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
ymean = 0
ysd = 2.5
y = norm_dist(x,ymean,ysd)

plt.scatter(x,y,color="blue")
plt.show()


# In practice, just use the pre-existing scipy.stats.norm:

# In[7]:


from scipy.stats import norm

x = np.linspace(-10,10,100)
zmean = 0
zsd = 2.5
z = norm.pdf(x,zmean,zsd)

plt.scatter(x,z,color="red")
plt.show()


# In[ ]:




