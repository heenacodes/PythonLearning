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


# In[7]:


df.Check.value_counts()


# In[9]:


df


# In[10]:


df['Employment'] == "Student, full-time"


# In[11]:


filt = (df['Employment'] == "Student, full-time")     #creating a filter


# In[12]:


df[filt]        #fetches all the columns for the filter


# In[18]:


df.loc[filt, ['Age', 'Employment']]    #fetching only specific columns from the filter result


# In[51]:


df["YearsCode"] = pd.to_numeric(df["YearsCode"], errors="coerce")              #YearsCode column is in string, hence converting it into numeric first
filt2 = (df['Employment'] == 'Student, full-time') & (df['YearsCode'] > 5)     #Filter with two condotions
df.loc[filt2, ['Employment', 'CodingActivities', 'YearsCode']]                   #Displaying the specifies columns of the filter


# In[37]:


df.loc[~filt2, ['Employment', 'CodingActivities', 'YearsCode']]        #Everything that is not part of the above filter


# In[42]:


countries = ['United States', 'India', 'United Kingdom', 'Canada']      #made a list of countries
filt3 = df['Country'].isin(countries)                                   #Passing the list in filter


# In[45]:


df.loc[filt3]


# In[54]:


filt4 = (df['LanguageHaveWorkedWith'].str.contains('Python', na = False))   #string operation filter


# In[55]:


df.loc[filt4, 'LanguageHaveWorkedWith']


# In[ ]:




