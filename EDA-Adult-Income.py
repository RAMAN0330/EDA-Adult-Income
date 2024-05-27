#!/usr/bin/env python
# coding: utf-8

# # Exploratoryt Data Analysis Of Adult Income Dataset

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


Data = pd.read_csv('adult.csv-Dataset/adult.data',header = None)


# In[3]:


Data.rename(columns={0:'age', 1:'workclass', 2:'fnlwgt', 3:'education', 4:'educational-num', 5:'marital-status', 6:'occupation', 7:'relationship', 8:'race', 9:'gender', 10:'capital-gain', 11:'capital-loss', 12:'hours-per-week', 13:'native-country', 14:'income'},inplace=True)


# In[4]:


Data.head(n = 5)


# In[5]:


Data.info()


# In[6]:


Data.describe


# In[7]:


Data.isna().sum()


# In[8]:


g_counts = Data['gender'].value_counts()
plt.bar(g_counts.index, g_counts, color=['skyblue', 'yellow'], edgecolor="black")
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender in Adult Income Dataset')
plt.show()


# In[9]:


sns.histplot(Data['age'], bins=20, kde=True)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age in Adult Income Dataset')
plt.show()


# **Bar Plot for Age vs Income**

# In[10]:


sns.barplot(x='age', y='income', data=Data, color="Cyan")
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Income According to Their Age')
plt.show()


# **Bar Plot for Education vs Income**

# In[11]:


sns.countplot(x='education', hue='income', data=Data)
plt.xticks(rotation=30, ha='right')
plt.xlabel('Education')
plt.ylabel('Income')
plt.title('Income According To Their Education')
plt.legend(title='Income Range', loc='upper right', labels=['<=50K', '>50K'])
plt.show()


# **Histogram for distribution of education-num and hours-per-week**

# In[12]:


features = ['educational-num', 'hours-per-week']
plt.figure(figsize=(14, 5))
for i, feature in enumerate(features, 1):
    plt.subplot(1, 3, i)
    sns.histplot(Data[feature].dropna(), bins=20, kde=True, color='green')
    plt.title(f'Distribution of {feature}')

plt.tight_layout()
plt.show()

