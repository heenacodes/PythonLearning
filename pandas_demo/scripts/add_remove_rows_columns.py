#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('../data/survey.csv')
schema_df = pd.read_csv('../data/schema.csv')  


# In[4]:


pd.set_option('display.max_columns', 150)
pd.set_option('display.max_rows', 150)


# In[30]:


df


# In[15]:


df['Intro'] = df['MainBranch'] + ' and ' + df['Employment']     #creating a new column
df.head(5)


# In[13]:


df.drop(columns='Intro', inplace=True)  #Deleting the column named 'Intro'


# In[14]:


df.head(5)


# In[20]:


df['Intro'] = df['MainBranch'] + ' & ' + df['Employment']     #creating a new column
df.head()


# In[29]:


df[['part1','part2']]= df['Intro'].str.split(' & ', expand=True)    #creating 2 new columns by splitting the existing column
df.head()


# In[28]:


df.drop(columns={'part1', 'part2'}, inplace=True)


# In[37]:


new_row = pd.DataFrame([{"ResponseId": "65438"}])

df = pd.concat([df, new_row], ignore_index=True)
df


# In[43]:


filt = (df['ResponseId'] == '65438')    #deleting the rows
df.drop(index = df[filt].index)


# In[ ]:




