#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


tugasbesar = pd.read_csv("iris.csv")
tugasbesar.head()


# In[4]:


cancer_sur = pd.read_csv("iris.csv", header=None, names=["age","opertaion_year","axil_nodes_det","surv_status"])
cancer_sur.head()


# In[5]:


print(cancer_sur.describe())


# In[43]:


sns.barplot(data=cancer_sur)


# In[22]:


sns.FacetGrid(cancer_sur,hue="surv_status",height = 5).map(sns.distplot,"age").add_legend()


# In[42]:


sns.scatterplot(data=cancer_sur)


# In[41]:


sns.kdeplot(data=cancer_sur)


# In[ ]:




