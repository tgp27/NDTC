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

# In[ ]:




