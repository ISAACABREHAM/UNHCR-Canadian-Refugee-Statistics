#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. From which countries has Canada admitted the most amount of refugees
# 2. What are the general trends from 2012 - 2022


# In[2]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


file_path = '/Users/ISAACABREHAM/Downloads/canada_refugee_stats.csv'


# In[7]:


data = pd.read_csv(file_path)


# In[8]:


data.info()


# In[15]:


toprefugees=data.groupby('Country-of-origin')['UNHCR-refugees'].sum().sort_values(ascending=False).head(10).reset_index(name='Total')


# In[21]:


plt.xticks(rotation=45)
sns.barplot(toprefugees, x='Country-of-origin', y='Total') 


# In[ ]:




