#!/usr/bin/env python
# coding: utf-8

# # DATA ANALYSIS PROJECT

# **Reading data using pandas**

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel('C:\DATA_SET\defaultOfCreditCardClients.xlsx')


# In[3]:


df.head()


# # Cleaning the data

# **Capitalize all the column names**

# In[4]:


df.columns = df.columns.str.upper()


# In[5]:


df.head()


# **Generating GENDER column using SEX column when value is 1 then MALE if value is 2 then FEMALE**

# In[6]:


df.loc[df["SEX"] == 1, "SEX"] = "MALE"


# In[7]:


df.loc[df["SEX"] == 2, "SEX"] = "FEMALE"


# In[8]:


df.loc[df["MARRIAGE"] == 1, "MARRIAGE"] = "MARRIED"
df.loc[df["MARRIAGE"] == 2, "MARRIAGE"] = "UNMARRIED"
df.loc[df["MARRIAGE"] == 3, "MARRIAGE"] = "OTHER"


# In[9]:


df.loc[df["EDUCATION"] == 1, "EDUCATION"] = "GRADUATE"
df.loc[df["EDUCATION"] == 2, "EDUCATION"] = "UNIVERSITY"
df.loc[df["EDUCATION"] == 3, "EDUCATION"] = "HIGH SCHOOL"
df.loc[df["EDUCATION"] == 4, "EDUCATION"] = "OTHERS"


# In[10]:


pay_map = {0: 'PAY DULY',-1: 'PAY DULY'}
df['PAY_0'] = df['PAY_0'].replace(pay_map)


# In[11]:


df.head()


# In[12]:


pay_map = {0: 'PAY DULY',-1: 'PREPAID 1', -2: 'PREPAID 2'}
df['PAY_2'] = df['PAY_2'].replace(pay_map)


# In[13]:


pay_map = {0: 'PAY DULY',-1: 'PREPAID 1', -2: 'PREPAID 2'}
df['PAY_3'] = df['PAY_3'].replace(pay_map)


# In[14]:


pay_map = {0: 'PAY DULY',-1: 'PREPAID 1', -2: 'PREPAID 2'}
df['PAY_4'] = df['PAY_4'].replace(pay_map)


# In[15]:


pay_map = {0: 'PAY DULY',-1: 'PREPAID 1', -2: 'PREPAID 2'}
df['PAY_5'] = df['PAY_5'].replace(pay_map)


# In[16]:


pay_map = {0: 'PAY DULY',-1: 'PREPAID 1', -2: 'PREPAID 2'}
df['PAY_6'] = df['PAY_6'].replace(pay_map)


# In[17]:


df.head()


# In[18]:


df = df.rename(columns={'PAY_0': 'PAID_APRL2005', 'PAY_2': 'PAID_MAY2005','PAY_3': 'PAID_JUNE2005', 'PAY_4': 'PAID_JULY2005',
                        'PAY_5': 'PAID_AUG2005', 'PAY_6': 'PAID_SEP2005'})


# In[19]:


df.head()


# In[20]:


df = df.rename(columns={'BILL_AMT6': 'BILL_APRL2005', 'BILL_AMT5': 'BILL_MAY2005','BILL_AMT4': 'BILL_JUNE2005', 'BILL_AMT3': 'BILL_JULY2005',
                        'BILL_AMT2': 'BILL_AUG2005', 'BILL_AMT1': 'BILL_SEP2005'})


# In[21]:


df.head()


# In[22]:


df = df.rename(columns={'PAY_AMT6': 'BILL_PAID_APRL2005', 'PAY_AMT5': 'BILL_PAID_MAY2005','PAY_AMT4': 'BILL_PAID_JUNE2005', 'PAY_AMT3': 'BILL_PAID_JULY2005',
                        'PAY_AMT2': 'BILL_PAID_AUG2005', 'PAY_AMT1': 'BILL_PAID_SEP2005'})


# In[23]:


df.head()


# In[24]:


df = df.rename(columns={'DEFAULT PAYMENT NEXT MONTH': 'DEFAULT_PAYMENT_NEXT_MONTH'})


# In[25]:


df.head()


# In[26]:


df = df.drop('DEFAULT_PAYMENT_NEXT_MONTH', axis=1)


# In[27]:


df.head()


# In[28]:


df['TOTAL_BILL'] = df[['BILL_SEP2005','BILL_AUG2005','BILL_JULY2005','BILL_JUNE2005','BILL_MAY2005','BILL_APRL2005']].sum(axis=1)


# In[29]:


df['TOTAL_BILL_PAID'] = df[['BILL_PAID_SEP2005','BILL_PAID_AUG2005','BILL_PAID_JULY2005','BILL_PAID_JUNE2005','BILL_PAID_MAY2005','BILL_PAID_APRL2005']].sum(axis=1)


# In[30]:


df.head()


# In[31]:


df.loc[:, 'DIFF_PERCENTAGE'] = (df['TOTAL_BILL_PAID'] / df['TOTAL_BILL'] * 100)


# In[32]:


df.head(10)


# In[33]:


def get_grade(DIFF_PERCENTAGE):
    if DIFF_PERCENTAGE >= 75:
        return 'STANDARD'
    elif DIFF_PERCENTAGE >= 50 and DIFF_PERCENTAGE < 75:
        return 'SUBSTANDARD 1'
    elif DIFF_PERCENTAGE >= 25 and DIFF_PERCENTAGE < 50:
        return 'SUBSTANDARD 2'
    else:
        return 'DEFAULTER'
    
    
df['CLASSIFICATION'] = df['DIFF_PERCENTAGE'].apply(lambda x: get_grade(x))


# In[36]:


df.head()


# In[35]:


df.to_excel('C:/DATA_SET/DEFAULT.xlsx', index=False)


