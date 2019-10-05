# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:01:09 2018

@author: adg49
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import optimize

b = 2.88e-3
h = 6.63e-34
c = 3e8
k = 1.38e-23

def black_body_dist(lam, T, constant):
    B = constant*2*h*c**2/lam**5*(np.exp(h*c/(lam*k*T))-1)**-1
    return B



pd.set_option('display.precision',2)

#reads the whole file except the first line
#If you only want a few columns of the file, read the whole file to a dataframe and then edit the dataframe in python
df = pd.read_csv(r'.\challenge notebooks\challenge_raw\rawData_Sun.csv',sep=',',skiprows=0)

#pd.options.display.float_format='{:.3f}'.format


#names the columns
df.columns = ['Wavelength','SpectralRadiance']

wl = df['Wavelength']
sr = df['SpectralRadiance']

#fit the raw data (wl, sr) to the black body function that we defined earlier, guessing that T = 6000 and constant = 2
#outputs the fitted values for T and constant
params, params_variance = optimize.curve_fit(black_body_dist, wl, sr, p0 = [6000, 2])

sr_fit = black_body_dist(wl, params[0], params[1])

#Add new column to dataframe
df['SpectralRadianceFit'] = sr_fit

#finds the index where the max radiance occurs, outputs the corresponding wavelength and assigns it to a variable
lam_max = wl[np.where(sr==np.max(sr))[0][0]]
#Calculates T using Wein's Law formula
T = b/lam_max

plt.plot(wl,sr)
plt.plot(wl,sr_fit)
#restrict plotting on x-axis
plt.xlim(0, 2000e-9)
#print(T)
#dst defines name and path of file
dst = r'.\results.csv'

#Exports df dataframe to csv file, with comma as separator, formatting with 3 decimal places
df.to_csv(dst,sep=',', float_format='%.3e')


