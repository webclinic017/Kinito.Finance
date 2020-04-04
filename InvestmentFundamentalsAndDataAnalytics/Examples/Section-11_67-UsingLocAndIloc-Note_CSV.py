#!/usr/bin/env python
# coding: utf-8
# In this lecture, we will introduce the two most frequently used **index selection methods** in Pandas – “loc” and “i-loc”. <br />
# An index selection method slices a table according to your preferences. It is a powerful feature of the Pandas package. What you have learned about dictionaries, lists, and NumPy will be very helpful here.
# 
# In the beginning, we will start by importing the NumPy and Pandas packages. 
# In[ ]:
import numpy as np
import pandas as pd
# Earlier in the course, we learned to randomize a matrix through the “rand-int” NumPy function. We will take advantage of this trick as we create a new Pandas Data Frame. 
# In[ ]:
np.random.randint(0,10,(6,4))
# We will choose a 6 by 4 matrix, and, pay attention, as we will assign a tuple whose values will act as the names of the rows of our table. It is better to call this tuple an **index**. That is, in the data table we create, we will have 6 rows called “a”, “b”, “c”, 1, 2, and 3 respectively. Finally, let’s call our columns “x”, “y”, 8, and 9.  The names we are using here are a bit strange, but they will help us explain the difference between using numbers or labels in an index.
# In[ ]:
df = pd.DataFrame(np.random.randint(0,10,(6,4)), 
                      index=('a','b','c','1','2','3'),
                      columns=['x','y', 8, 9])
# So, this is the new table. It contains 6 rows and 4 columns. 
# In[ ]:
df
# Here are the two main methods we will need. 
# “Loc” is label based. This means that within the brackets (also called an indexing operator), you will have to indicate label values. In this data frame, all the row names are labels. So, should I decide to access the row with index 1, I must type “d.f.” dot “loc” and 1 in quotes within the brackets. 
# And here is the data that we managed to extract, ordered vertically. 
# In[ ]:
df.loc['1']
# “Loc” with an index “b”, instead, will extract row “b”. And so on and so forth.
# In[ ]:
df.loc['b']
# Had I written “d.f.” dot “loc” and 1 in the brackets, with no quotes, we would have run into an error. 
# In[ ]:
df.loc[1]
# Why? Because we did not designate 1 as a label. We put the number 1 within brackets. It is an integer, to be more precise. Values that are not marked as labels do not work properly with “loc”. 
# ****
# The “i-loc” method is position based. It is not, so to speak, labels driven. “I-loc” follows the classical Pythonic logic about indexing - the same as the one we used for slicing lists. In other words, we count from 0, and the colon symbol helps us when we specify rows or columns for extraction.
# In[ ]:
df.iloc[1]
# Of course, a few examples will clarify when and how to use each of the two methods.
# “I-loc” with an index from 1 to 4 will include rows 2, 3, and 4. Alternatively, the rows at positions 1, 2, and 3, right? 
# In[ ]:
df.iloc[1:4]
# If we leave colon 3 in the brackets, we will get the first 3 rows – the rows indexed 0, 1, and 2. So, we must follow the same rules as the ones we applied when slicing lists.
# In[ ]:
df.iloc[:3]
# In the data table, we also have columns. The cell we just executed could have provided the same result if we had added a comma and a colon here. A single colon, without a number on any of the two sides, means we are interested in all the columns of the indicated row. 
# In[ ]:
df.iloc[:3, :]
# Naturally, a sole colon before the comma, and then a column selection “colon 2”, will select the entire first and second columns of this data frame.
# In[ ]:
df.iloc[:,:2]
# Good. Now, for the sake of comparison, turning briefly to the “loc” method, this piece of code will extract all the rows until the one labeled with 2. 
# In[ ]:
df.loc[:'2']
# Meanwhile, the line of code you see here will give me the rows corresponding to the indices ‘c’, 1, and 2. This example shows that “loc” can be helpful in certain situations. 
# In[ ]:
df.loc['c':'2']
# In a bigger data table, where your data has been indexed with names, “loc” will help you point the rows that refer to the respective label names. For instance, in another data set, organized for all states, you could say “mark the data from “Arizona” to “Indiana” for me” placing the names within quotes in the parentheses after the “loc” method. 
# ******************
# Things get trickier when we have an integer based index. That is an index without explicit labels such as “a”, “b”, or “c”. 
# In this second data frame, we will use the integers 54, 55, 56, 1, 2, and 3 as row names, as this will allow us to explain the difference between “loc” and “i-loc” more easily.
# In[ ]:
df2 = pd.DataFrame(np.random.randint(0,10,(6,4)), 
                      index=(54, 55, 56, 1, 2, 3),
                        columns=['x','y', 8, 9])
# Knowing there are no strings in the index of this data frame, “loc” will function with integer values within the brackets, using no quotes. However, still, it wouldn’t be a substitute of “i-loc” and, please, be very careful about that!
# In[ ]:
df2
# “Loc” until 2 will deliver a table containing all the rows up until the one whose index is 2. That is, we will have 5 rows in the newly created frame.
# In[ ]:
df2.loc[:2]
# With the same code within the brackets, “i-loc” will extract the first two rows of the second data frame – the rows indexed with 0 and 1. 
# In[ ]:
df2.iloc[:2]
# This was a very delicate topic, believe me. There are tens of pages on the internet about index selection methods. It is important for you to understand the subtle difference between “loc” and “i-loc” so that you approach harder financial and data science tasks with ease. 
# Now, roll up your sleeves and do the following exercise!
# *******
# Exercises:
# In[ ]:
df['x']
# In[ ]:
df.loc[:,'x']
# In[ ]:
df[8]
# ****
# In[ ]:
from pandas_datareader import data as wb
# In[ ]:
PG = pd.read_csv('D:/Python/PG_1995-03_23_2017.csv', index_col = 'Date')
# In[ ]:
PG.head()
# In[ ]:
PG.loc['1995-01-03', 'Open']
# In[ ]:
PG.iloc[0,5]
# *****
# In[ ]:
df3 = pd.DataFrame(np.random.randint(0,10,(6,4)), columns=['x','y', 8, 9])
# In[ ]:
df3
# In[ ]:
df3.loc[0:3]
# In[ ]:
df3.iloc[0:3]
# In[ ]:
df3.loc[0:3,:'y']
# In[ ]:
df3.iloc[0:3,1]
