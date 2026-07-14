#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[20]:


df = pd.read_csv('../data/survey.csv', index_col='ResponseId')     #setting the index as the column 'ResponseId'
schema_df = pd.read_csv('../data/schema.csv',index_col = 'qname')  #setting the index as the column 'qname'


# In[15]:


pd.set_option('display.max_columns', 150)
pd.set_option('display.max_rows', 150)


# In[16]:


df.head()


# In[11]:


df.columns.to_list()


# In[18]:


df.loc[1]        #fetching the value of index whose value is 1. i.e. column 'ResponseId' with value 1


# In[22]:


schema_df


# In[25]:


schema_df.loc['CodingActivities']   #displays a row with index matching 'CodingActivities'. Displays all the columns


# In[27]:


schema_df.loc['CodingActivities', 'question']    #displays the specified column for the given index value


# In[28]:


schema_df.sort_index()        #indexes are sorted alphabetically


# In[29]:


schema_df.sort_index(ascending=False)   #sorts the indexes in the descending order   


# In[35]:


schema_df.sort_index(inplace=True, ascending=False)     #sorts the indexes permanently


# In[36]:


schema_df


# In[ ]:




