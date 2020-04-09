#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# <center>*Copyright Pierian Data 2017*</center>
# <center>*For more information, visit us at www.pieriandata.com*</center>

# # Introduction to Statsmodels
# 
# Statsmodels is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. An extensive list of result statistics are available for each estimator. The results are tested against existing statistical packages to ensure that they are correct. The package is released under the open source Modified BSD (3-clause) license. The online documentation is hosted at statsmodels.org.
# 
# The reason we will cover it for use in this course, is that you may find it very useful later on when discussing time series data (typical of quantitative financial analysis).
# 
# Let's walk through a very simple example of using statsmodels!

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


# You can safely ignore the warning:
#  Please use the pandas.tseries module instead. from pandas.core import datetools
import statsmodels.api as sm


# In[19]:


df = sm.datasets.macrodata.load_pandas().data


# In[20]:


print(sm.datasets.macrodata.NOTE)


# In[21]:


df.head()


# In[22]:


index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))


# In[23]:


df.index = index


# In[24]:


df.head()


# In[26]:


df['realgdp'].plot()
plt.ylabel("REAL GDP")


# ## Using Statsmodels to get the trend
# The Hodrick-Prescott filter separates a time-series  y_t  into a trend  τ_t and a cyclical component  ζt
# 
# $y_t = \tau_t + \zeta_t$
# 
# The components are determined by minimizing the following quadratic loss function
# 
# $\min_{\\{ \tau_{t}\\} }\sum_{t}^{T}\zeta_{t}^{2}+\lambda\sum_{t=1}^{T}\left[\left(\tau_{t}-\tau_{t-1}\right)-\left(\tau_{t-1}-\tau_{t-2}\right)\right]^{2}$

# In[30]:


# Tuple unpacking
gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df.realgdp)


# In[31]:


gdp_cycle


# In[29]:


type(gdp_cycle)


# In[36]:


df["trend"] = gdp_trend


# In[37]:


df[['trend','realgdp']].plot()


# In[41]:


df[['trend','realgdp']]["2000-03-31":].plot(figsize=(12,8))


# ## Great job!
