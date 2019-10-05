#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
import numpy as np
import matplotlib.pyplot as plt

raw_dir = '.\challenge_raw'
# file = 'rawPlanck_2000.txt'
# file_path = os.path.join(raw_dir,file)

# test_data = np.loadtxt(file_path, skiprows=2, delimiter='\t')
# wv = test_data[:,0]
# B = test_data[:,1]
# plt.plot(wv,B)
# plt.show()


str1 = 'rawPlanck_'
str2 = '.txt'

tmp = np.linspace(2000,8000,13)

integ_arr = np.array([])
for T in tmp:
    file_str = ''.join([str1,str(int(T)),str2])
    file_path = os.path.join(raw_dir,file_str)
    
    data = np.loadtxt(file_path,skiprows=2, delimiter='\t')
    wv= data[:,0]
    B = data[:,1]
    # get max value
    integ = np.trapz(B,x=wv)
    integ_arr = np.append(integ_arr, integ)

    



plt.plot(np.log(tmp),np.log(integ_arr))
plt.show()

m,c = np.polyfit(np.log(tmp),np.log(integ_arr),1)
print(m,c)
print(np.exp(c))

sigma_arr = np.log(integ_arr) - 4*np.log(tmp)
# print(sigma_arr)
sigma = np.mean(sigma_arr)
print(np.pi*np.exp(sigma))


# In[ ]:





# In[ ]:




