#!/usr/bin/env python
# coding: utf-8

# # New York City Airbnb Open Data

# In[1]:


#Importing necessary libraries
import pandas as pd
import numpy as np


# In[2]:


#load the dataset
df = pd.read_csv("AB_NYC_2019.csv")


# In[5]:


#Basic information about the database 
print("Basic Dataset info:")
df.info()


# In[16]:


#Checking for missing values
print("\nMissing values:")
df.isnull().sum()


# In[18]:


#Checking for duplicate rows
print("\nNumber of duplicates in the dataset:",df.duplicated().sum())


# In[26]:


#Data integrity 


# In[24]:


# describing numerical data for basic integrity checks
print("\nData integrity check (Range of values in critical columns):")
print(df[['price','minimum_nights','availability_365']].describe())


# In[25]:


# checking for out-of-range values
outlier_check = df[(df['price']<0) | (df['minimum_nights']<0)]
print("\nOut-of-range values (if any):")
print(outlier_check)


# In[27]:


# Missing data handling


# In[28]:


#fill missing 'name' and 'host_name' with 'Unknow'
df['name'].fillna('Unknow',inplace=True)
df['host_name'].fillna('Unknown',inplace=True)


# In[30]:


#fill missing 'reviews_per_month' with 0(assuming no reviews)
df['reviews_per_month'].fillna(0,inplace=True)


# In[31]:


#fill missing 'last_review' with a placeholder
df['last_review'].fillna('NO Reviws',inplace=True)


# In[32]:


#Re-check missing values
print("\nMissing values after filling:")
print(df.isnull().sum())


# In[36]:


#Duplicate removal (if any duplicates are found)
df.drop_duplicates(inplace=True)
print("\nNumber of duplicates after removal:",df.duplicated().sum())


# In[37]:


#Standardization of text dara('name and 'host_name')
df['name']=df['name'].str.title()
df['host_name']=df['host_name'].str.title()


# In[38]:


#verify check 
print("\nnSample of standardized'name' and 'host_name':")
print(df[['name','host_name']].head())


# In[40]:


#Outlier Detection using IQR method


# In[42]:


#function to detect outliers
def detect_outliers(df,column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]


# In[45]:


# Detect outliers in 'price' and 'minimum_nights'
price_outliers = detect_outliers(df, 'price')
min_nights_outliers = detect_outliers(df, 'minimum_nights')


# In[48]:


# Output the results


# In[49]:


print("\nPrice Outliers (first 5 rows):")
print(price_outliers[['id', 'price']].head())


# In[50]:


print("\nMinimum Nights Outliers (first 5 rows):")
print(min_nights_outliers[['id', 'minimum_nights']].head())


# In[52]:


#Final Check on Clean Data
print("\nFinal Dataset Info After Cleaning:")
df.info()


# In[ ]:




