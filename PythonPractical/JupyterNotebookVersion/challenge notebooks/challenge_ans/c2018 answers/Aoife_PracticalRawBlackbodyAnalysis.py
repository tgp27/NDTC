import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import optimize

#defining the file endings that we are going to cycle through
file_endings = list(range(2000, 8500,500))

#define the colours we will cycle through for the plot - we want to have a redder colour for higher temps
cmap = plt.get_cmap('coolwarm')

wien_arr = np.array([])
total_rad = np.array([])

h = 6.63e-34
c = 3e8
k = 1.38e-23

def black_body_dist(lam, T):
    B = 2*h*c**2/lam**5*(np.exp(h*c/(lam*k*T))-1)**-1
    return B

for i in file_endings:
    src = r'.\challenge notebooks\challenge_raw\rawPlanck_' + str(i) + '.txt'
    df = pd.read_csv(src,sep='\t',header=0)
    wl = df['Wavelength']
    sr = df['SpectralRadiance']
    
    colour = cmap(i/file_endings[-1])
    
    params, params_variance = optimize.curve_fit(black_body_dist, wl, sr, p0 = [i])
    #print(params, params_variance)
    sr_fit = black_body_dist(wl, params[0])
    
    #np.where outputs the number of the index where the condition is satisfied.
    lam_max = wl[np.where(sr_fit==np.max(sr_fit))[0][0]]
    wien_arr = np.append(wien_arr, lam_max)
    
#    plt.plot(wl, sr, label = str(i)+'K', c = colour)
#    plt.plot(wl, sr_fit, '--', label = str(i) + 'K fit', c = colour)
    
    total_rad = np.append(total_rad, np.pi*np.trapz(sr,wl))
    
#plt.ticklabel_format(style='sci', axis = 'x', scilimits=(0,0))
#plt.xlim(0, 1.5e-6) 
#plt.legend()
#plt.show()


temp = np.array(file_endings)
inverse_temp = np.reciprocal(np.float32(temp))
log_temp = np.log(np.float32(temp))

log_rad = np.log(total_rad)

plt.plot(log_rad, log_temp)
m,c = np.polyfit(log_temp, log_rad, 1)

print('n =', m, 'and sigma =', np.exp(c))  



#print(temp)
#print(inverse_temp)
#print(wien_arr)
#plt.plot(inverse_temp, wien_arr)


plt.show()

#print(np.polyfit(inverse_temp, wien_arr, 1))



    
    
    

# choosing data format
#pd.options.display.float_format = '{:.1f}'.format
# show first 5 values
#print(df.head())

