#!/usr/bin/env python
# coding: utf-8
# Theoretically, a distribution of a statistical dataset shows us the frequency at which possible values occur within an interval. 
# 
# There are many statistical distributions, and the most popular ones have their own names. In this notebook file, we will focus on one of them - the normal distribution, also called Gaussian distribution. 
# 
# The examples we show will best clarify the concept.
# To begin, import NumPy, Matplotlib Pyplot, the "norm" module from "scipy.stats", and matplotlib inline.
# In[1]:
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')
# In one of our earlier lectures, we learned how to create random numbers with np.random.random() and np.random.randint(). This time, we will use NumPy to create a random normal distribution:
# In[2]:
normal_d = np.random.normal(10,5,40)
normal_d
# In parentheses, we specified the mean value around which the distribution will be centered. We chose it to be 10. Next, the standard deviation will be equal to 5. This is why, when you skim through the numbers within the array, you will see they are all around 10 and rarely less than 5 or greater than 15.  <br/>
# 
# The last argument within the parentheses shows the number of observations generated by NumPy - 40. This is why the obtained one-dimensional array contains 40 values. Great!
# ***
# A specific case of the normal distribution is the standard normal distribution. This is a special case when the mean value of the distribution is 0 and the standard deviation equals 1. <br/>
# 
# NumPy provides a tool for generating random numbers from a standard normal distribution. This time, you need not specify a mean and a standard deviation value in parentheses. Typing a single argument of 40 in parentheses will provide a one-dimensional array with 40 elements.   
# In[3]:
std_norm = np.random.standard_normal(40)
std_norm
# If you would like to create a two-dimensional array with standard-normally distributed values, double the parentheses and designate the dimension in the following way:
# In[4]:
std_norm_2 = np.random.standard_normal((4,10))
std_norm_2
# *************
# Now, let's see how the obtained std_norm result looks when plotted on a graph.
# In[5]:
plt.plot(std_norm)
plt.show()
# This is a line chart. The line connects all the points obtained in the *std_norm* array, reading the numbers from left to right and from top to bottom. <br/>
# 
# You can see all the values are around 0, and they rarely leave the interval [-1;1]. <br/>
# *************
# The next graph shows you the probability with which the data points from a designated range are expected to occur. Hence, the function we will use is called probability density function, and it best exhibits the characteristics of a certain distribution. The probability density function of the normal distribution is contained in the 'scipy.stats' module.  <br/>
# 
# First, we must set the interval within which we would like to distribute our data. The arguments, -5 and 5, designate the end points of the range. The third argument, 0.01, specifies the distance between two adjacent values.
# In[6]:
range = np.arange(-5, 5, 0.01)
# Finally, we will plot data from this range with a mean of 0 and a standard deviation of 1.
# In[7]:
plt.plot(range, norm.pdf(range, 0, 1))
# The obtained curve is informally referred to as a bell-curve. It corresponds to the shape of any normal distribution.<br/>
# 
# A typical feature of this distribution is its bell-curve is symmetrical. This means most observations will equal the mean value of the distribution, and there will be as many observations below the mean as there will be above it. The mean value is in the center of the graph. That the two ends of the curve are closer to the x-axis is explained by the rare occurrence of observations that largely deviate from the center.
# ***
# The normal distribution is important for statisticians because distributing a dataset containing 250 or more observations can be approximated to a normal distribution. Therefore, this distribution is used frequently. In our next lectures, we will run tests with hundreds, and even thousands, of data points, and we will often need to apply this technique.
