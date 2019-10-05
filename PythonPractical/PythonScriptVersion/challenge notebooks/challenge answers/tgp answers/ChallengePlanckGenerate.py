#!/usr/bin/env python
# coding: utf-8

# ## Not the actual generate file, that was accidentally deleted. Replica.

# In[4]:



import os
import numpy as np
import matplotlib.pyplot as plt

raw_dir = '.\challenge_raw'


c = 3.00e8
h = 6.63e-34
kb = 1.38e-23

def Bspec(wv,temp):
    pref = (2*h*c**2)/(wv**5)
    expo = (h*c)/(wv*kb*temp)
    
    B = pref*(np.exp(expo)-1)**(-1)
    
    return B


def Wspec(wv,temp):
    """
    Wien approximation
    """
    pref = (2*h*c**2)/(wv**5)
    expo = (h*c)/(wv*kb*temp)
    B = pref*np.exp(-expo)
    
    return B

wv = np.linspace(100e-9,5000e-9,200)
B = Bspec(wv,5000)
Bw = Wspec(wv,5000)
plt.plot(wv,B)
plt.plot(wv,Bw)
plt.show()


## then lognormal dist, mean 0, sigma 0.07



# In[ ]:





# In[ ]:




