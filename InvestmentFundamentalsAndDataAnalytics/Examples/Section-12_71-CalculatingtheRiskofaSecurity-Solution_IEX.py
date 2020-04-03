#!/usr/bin/env python
# coding: utf-8

# ## Calculating the Risk of a Security

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Download the data for Microsoft (‘MSFT’) from IEX for the period ‘2015-1-1’ until today. <br />
# Assess the daily and the annual risk of ‘MSFT’. Repeat the exercise for Apple for the same timeframe. 

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


tickers = ['MSFT', 'AAPL']

data = pd.DataFrame()

for t in tickers:
    data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1')['close']


# In[3]:


returns = np.log(data / data.shift(1))
returns


# ### MSFT

# Daily risk:

# In[4]:


returns['MSFT'].std()


# Annual risk:

# In[5]:


returns['MSFT'].std() * 250 ** 0.5


# ### Apple

# Daily risk:

# In[6]:


returns['AAPL'].std()


# Annual risk:

# In[7]:


returns['AAPL'].std() * 250 ** 0.5


# ******

# Store the volatilities of the two stocks in an array called "vols".

# In[8]:


vols = returns[['MSFT', 'AAPL']].std() * 250 ** 0.5
vols


# How are the two risk values different?
