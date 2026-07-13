#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/survey.csv')
schema_df = pd.read_csv('../data/schema.csv')


# In[3]:


pd.set_option('display.max_column', 150)
pd.set_option('display.max_rows', 150)


# In[4]:


df.head(10)


# In[5]:


df['MainBranch']  #printing any one column. This is preferable in case the the df.function has the same name as column name. e.g if there is column name 'count', ti conflicts with df method count


# In[6]:


df.MainBranch


# In[7]:


type(df['MainBranch'])


# In[9]:


df[['MainBranch','Age','Employment']] #printing more than once column of the DataFrame


# In[10]:


df.columns #prints all the columns


# In[11]:


df.iloc[0]


# In[12]:


df.iloc[[0,1]]  #printing more than one specified number of rows


# In[13]:


df.loc[[0,1], ['MainBranch', 'Age', 'Employment']]    #printing the specified rows and specified columns


# In[14]:


df['MainBranch'].value_counts()       #counts the number of distinct values


# In[15]:


df.loc[0, 'RemoteWork']              #return the value for column 'RemoteWork' in row number 0

