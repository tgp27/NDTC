#!/usr/bin/env python
# coding: utf-8

# # Numerical Integration
# 
# ## Estimating integral of a given function with limits

# ### Integrating data
# NumPy can integrate a given array of data. For example, let's create a normal distribution with mean 0.0 and standard deviation 2.5.

# In[67]:


from scipy.stats import norm
import numpy as np

xval = np.linspace(-10,10,100)
ymean = 0
ysd = 2.5
yval = norm.pdf(xval,ymean,ysd)


# The area under this function should be very close to 1.0, since it's normalised. We estimate the value using the [trapezium rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) (aka trapezoidal rule), implemented by the numpy.trapz function. More info on this Python function [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.trapz.html)

# In[82]:


eval = np.trapz(yval,x=xval)
print(eval)


# The value is very close to 1.0, as expected.

# There is another way to implement the trapezium rule, using the scipy.integrate.cumtrapz function. Unlike the np.trapz function, it gives cumulative values.
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.integrate.cumtrapz.html#scipy.integrate.cumtrapz

# In[81]:


import scipy.integrate as integrate
# from scipy.stats import norm
# import numpy as np

# xval = np.linspace(-10,10,100)
# ymean = 0
# ysd = 2.5
# yval = norm.pdf(xval,ymean,ysd)

cum_eval = integrate.cumtrapz(yval,xval)
print(cum_eval[-1])


# The output "cum_eval" is an array of values with the cumulative integral values (print out cum_eval to see what I mean). The final value is what we want. You can see that it's identical (to over 10 decimal places) to the np.trapz value; both functions implement exactly the same algorithm, so they produce the same numerical estimate.

# There are other, more sophisticated numerical integral methods that can also be implemented in Python, such as [Simpson's rule](http://mathworld.wolfram.com/SimpsonsRule.html). See e.g. [SciPy documentation](https://docs.scipy.org/doc/scipy-0.14.0/reference/integrate.html) for more info.

# ### Smooth function, finite limits

# For example, we want to evaluate
# $$ \int_0^3 x^2 \mbox{d}x = \left[ \frac{1}{3}x^3\right]_0^3 = 9$$
# We will use the scipy.integrate.quad function. More info on quad [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html#scipy.integrate.quad)

# In[69]:


import scipy.integrate as integrate

eval, err = integrate.quad(lambda x: x**2, 0, 3)


# The outputs are
# - "eval", the evaluated result
# - "err", the estimated absolute error (uncertainty) in the result
# 
# For this simple integral, we get a result quickly with very low error:

# In[70]:


print(eval)


# In[71]:


print(err)


# ### Smooth function, infinite limits

# Now we will try an integral with an infinite limit:
# $$ \int_0^\infty \sin(x)~e^{-2x}~ \mbox{d}x  = \frac{1}{5}$$
# Infinity is coded using the numpy variable np.inf.

# In[72]:


eval, err = integrate.quad(lambda x: np.sin(x)*np.exp(-2*x), 0, np.inf)


# In[73]:


print(eval,err)

