#!/usr/bin/env python
# coding: utf-8
# ## Running a Multivariate Regression in Python
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Let’s continue working on the file we used when we worked on univariate regressions.
# *****
# Run a multivariate regression with 5 independent variables – from Test 1 to Test 5.
# In[ ]:
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm 
import matplotlib.pyplot as plt
# In[ ]:
data = pd.read_excel('D:/Python/Data_Files/IQ_data.xlsx')
# In[ ]:
data
# ### Multivariate Regression:
# Independent Variables: *Test 1, Test 2, Test 3, Test 4, Test 5*
# In[ ]:

# In[ ]:

# The p-value of the variable Test 1 in the univariate regression looked very promising. Is it still low? If not – what do you think would be the reason for the change?
# ********
# Try regressing Test 1 and Test 2 on the IQ score first. Then, regress Test 1, 2, and 3 on IQ, and finally, regress Test 1, 2, 3, and 4 on IQ. What is the Test 1 p-value in these regressions?
# Independent Variables: *Test 1, Test 2*
# In[ ]:

# In[ ]:

# Independent Variables: *Test 1, Test 2, Test 3*
# In[ ]:

# In[ ]:

# Independent Variables: *Test 1, Test 2, Test 3, Test 4*
# In[ ]:

# In[ ]:

# It seems it increases a lot when we add the result from Test 4. 
# ****
# Run a regression with only Test 1 and Test 4 as independent variables. How would you interpret the p-values in this case?
# Independent Variables: *Test 1, Test 4*
# In[ ]:

# In[ ]:

# Independent Variables: *Test 4*
# In[ ]:

# In[ ]:

# ***Suggested Answer:***
# *Test 1 and Test 4 are correlated, and they contribute to the preparation of the IQ test in a similar way.*