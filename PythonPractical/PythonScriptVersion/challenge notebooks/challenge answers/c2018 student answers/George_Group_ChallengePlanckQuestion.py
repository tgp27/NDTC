#!/usr/bin/env python
# coding: utf-8

# # Black-body distribution
# 
# The spectral radiance $B$ of a spherical black body (ideal non-reflective object) at a wavelength $\lambda$ and temperature $T$ is given by
# 
# $$
# B(\lambda, T) = \frac{2 hc^2}{\lambda^5}\left[\exp\left( \frac{hc}{\lambda k_B T}\right) - 1\right]^{-1}
# $$
# 
# where (in SI units) $h = 6.63\times 10^{-34}$ is Planck's constant, $c = 3.00\times10^{8}$ is the speed of light and $k_B = 1.38\times10^{-23}$ is Boltzmann's constant.
# 
# [Example spectra](https://www.periodni.com/gallery/blackbody_radiation.png
# ) for various temperatures.
# 
# I have generated some noisy data for $B(\lambda, T)$ at various temperatures, which can be found as txt files in the challenge_raw folder.
# 
# ## Wien Law
# The maximum of $B(\lambda,T)$ occurs at some wavelength $\lambda_{max}$ that depends on the temperature $T$. The two quantities are related by Wien's law:
# 
# $$
# \lambda_{max} = \frac{b}{T}
# $$
# 
# where $b$ is some constant. Determine $b$.
# 
# ## Stefan-Boltzmann Law
# 
# The total radiance $R$ across all solid angles is given by
# 
# $$
# R(T) = \pi \int_0^{\infty} \mbox{d}\lambda ~ B(\lambda,T)
# $$
# 
# The radiance has a simple relationship with temperature (the Stefan-Boltzmann law)
# 
# $$
# R = \sigma T^n
# $$
# 
# where $\sigma$ and $n$ are constants. Determine $n$ and $\sigma$ by performing a numerical integration of each set of data.
# 
# ## Solar spectrum
# 
# In the raw data folder (.\challenge_raw) there is some real spectral data for the Sun (.csv file). Estimate the temperature of the Sun's surface by comparing the solar spectrum to a black-body spectrum.
# 

# In[82]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

#Function to fit
h = 6.63e-34
c = 3e8
k = 1.38e-23
def black_body_dist(lam, T):
    B = 2*h*c**2/lam**5*(np.exp(h*c/(lam*k*T))-1)**-1
    return B

# Define things for iterating over
file_endings = list(range(2000,8500,500))
cmap = plt.get_cmap('coolwarm')
wien_arr = np.array([])
rs = np.array([])

for i in file_endings:
    src = r'.\challenge_raw\rawPlanck_' + str(i) + '.txt'
    df = pd.read_csv(src,sep='\t',header=0)
    wl = df['Wavelength']
    sr = df['SpectralRadiance']
    
    # Fit data
    params, params_covariance = optimize.curve_fit(black_body_dist, wl, sr, p0=[i])
    sr_fit = black_body_dist(wl,params[0])
    
    # Colours
    colour = cmap(i/file_endings[-1])
    
    # Plot data
    plt.plot(wl, sr, label = str(i) + 'K', c = colour)
    plt.plot(wl, sr_fit, '--', label = str(i) + 'K fit', c = colour)
    
    # Wien's law
    sr_max = np.max(sr_fit)
    lam_max = wl[np.where(sr_fit == sr_max)[0][0]]
    wien_arr = np.append(wien_arr, lam_max)
    
    # Integration
    r = np.trapz(sr,wl)*np.pi
    rs = np.append(rs, r)

# Format spectral plot
plt.xlabel('Wavelength / m')
plt.ylabel('Spectral Radiance / units')
plt.xlim(0,1.5e-6)
plt.ticklabel_format(style='sci', axis = 'x', scilimits=(0,0))
plt.legend(['Data','Fit'])
plt.show()

# Wein plot
temp = np.float32(file_endings)
inv_T = np.array(temp)**-1
plt.plot(inv_T, wien_arr)
plt.xlabel('1/T')
plt.ylabel('Lambda Max')
plt.ticklabel_format(style='sci', axis = 'x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis = 'y', scilimits=(0,0))
plt.show()
b, intercept = np.polyfit(inv_T, wien_arr, 1)
print('b =',b)

# Stefan Boltzmann
log_temp = np.log(temp)
log_r = np.log(rs)
plt.plot(log_temp, log_r)
plt.xlabel('log(T)')
plt.ylabel('log(R)')
plt.show()
m, c = np.polyfit(log_temp, log_r, 1)
n = m
sigma = np.exp(c)
print('n = ',n, ' and sigma = ', sigma)


# In[ ]:




