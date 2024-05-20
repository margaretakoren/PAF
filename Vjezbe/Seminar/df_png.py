#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi

df = pd.read_csv('double_pendulum_data.csv')
df_10 = df.head(10)
df_10


# In[2]:


#df_10 = df_10.style.background_gradient()


# In[3]:


dfi.export(df_10, 'df_image.png', table_conversion='matplotlib')

