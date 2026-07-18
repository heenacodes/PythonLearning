#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/survey.csv')
schema_df = pd.read_csv('../data/schema.csv')  


# In[3]:


pd.set_option('display.max_columns', 150)
pd.set_option('display.max_rows', 150)


# In[4]:


df.Check.value_counts()           #returns the count of the given column


# In[5]:


df


# In[6]:


df.columns.to_list()


# In[7]:


df.apply(len)  


# In[8]:


df.apply(len, axis = 'columns')


# In[9]:


df['RemoteWork'] = df['RemoteWork'].str.lower()


# In[10]:


df


# In[11]:


df['Country'] = df['Country'].replace('India','Bharat')


# In[12]:


filt = (df['Country'] == 'Bharat')
df[filt]


# In[13]:


df['Country'] = df['Country'].replace({'Bharat': 'India', 'Canada': 'Canneda', 'United States of America': 'USA' })


# In[14]:


countries = ['India', 'Canneda', 'USA']
filt2 = df['Country'].isin(countries)
df[filt2]


# In[17]:


df['Country'] = df['Country'].replace('Canneda','Canada')
filt = (df['Country'] == 'Canada')
df[filt]


# In[23]:


df.rename(columns={'CompTotal':'Salary'}, inplace= True)    #renaming column 'CompTotal' with 'Salary'
df['Salary']


# In[29]:


df['SOAccount'].map({'Yes':'True', 'No': 'False'})   # Mapping Yes and No values to True and False respectively
df['SOAccount']


# In[ ]:




