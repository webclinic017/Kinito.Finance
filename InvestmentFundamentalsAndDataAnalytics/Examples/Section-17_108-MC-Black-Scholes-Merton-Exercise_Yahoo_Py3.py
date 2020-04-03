#!/usr/bin/env python
# coding: utf-8

# ## Monte Carlo - Black-Scholes-Merton

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Download the data for Microsoft (‘MSFT’) from Yahoo Finance for the period ‘2000-1-1’ until today.

# We have written a few lines of code that will import the documents you need and define the functions estimating d1, d2, and the Black-Scholes-Merton formula. 

# In[ ]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

ticker = 'MSFT'  
data = pd.DataFrame()  
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2000-1-1')['Adj Close']


# In[ ]:


def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
 
def d2(S0, K, r, sigma, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

def BSM(S, K, r, stdev, T):
        return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))


# Store the annual standard deviation of the log returns in a variable, called “stdev”.

# In[ ]:





# Set the risk free rate, r, equal to 2.5% (0.025); the strike price, K, equal to 110.0; and the time horizon, T, equal to 1, respectively.

# In[ ]:





# Create a variable S equal to the last adjusted closing price of Microsoft. Use the “iloc” method.

# In[ ]:





# Call the d1 and d2 functions with the relevant arguments to obtain their values.

# In[ ]:





# In[ ]:





# Use the BSM function to estimate the price of a call option, given you know the values of S, K, r, stdev, and T.

# In[ ]:




