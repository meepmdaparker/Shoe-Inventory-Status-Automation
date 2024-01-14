#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel('Shippable.xlsx')


# In[3]:


df.info()


# In[4]:


df['Gender'].unique()


# In[5]:


df['Whole Sizes Only vs Half and Whole'].unique()


# In[ ]:


#Test Draft
"""
kidswholeL = ['5', '6', '7', '8', '9', '10']
kidsL = ['5', '5H', '6', '6H', '7', '7H', '8', '8H', '9', '9H', '10']
kidswholeN = ['1O', '11', '12', '13', '1', '2']
kidsN = ['10H', '11', '11H', '12', '12H', '13', '13H', '1', '1H', '2', '2H']
menswhole = ['9', '10', '11']
mens = ['8H', '9', '9H', '10', '10H', '11']
wmnswhole = ['6', '7', '8']
wmns = ['6H', '7', '7H', '8', '8H']




for i in range(len(df)):
if df['Gender'] = "BOYBOYS": or df['Gender'] = 'GIRLGIRLS'
    if df['L,N'] = 'L'
        if df['Whole Sizes Only vs Half and Whole'] = 'Whole Sizing':
            df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in kidswholeL) else '', axis=1)

        else:
            df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in kidsL) else '', axis=1)

    elif df['L,N'] = 'N':
        if df['Whole Sizes Only vs Half and Whole'] = 'Whole Sizing':
            df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in kidswholeN) else '', axis=1)

        else:
            df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in kidsN) else '', axis=1)


elif df['Gender'] = 'MENMENS'
    if df['Whole Sizes Only vs Half and Whole'] = 'Whole Sizing':
        df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in menswhole) else '', axis=1)

    else:
        df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in mens) else '', axis=1)

elif df['Gender'] = 'WMNWOMENS'
    if df['Whole Sizes Only vs Half and Whole'] = 'Whole Sizing':
        df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in wmnswhole) else '', axis=1)

    else:
        df['Status'] = df.apply(lambda row: 'broken' if any(row[col] == 0 or pd.isnull(row[col]) for col in wmns) else '', axis=1)

"""


# In[8]:


kidswholeN = ['5', '6', '7', '8', '9', '10']
kidsN = ['5', '5H', '6', '6H', '7', '7H', '8', '8H', '9', '9H', '10']
kidswholeL = ['10', '11', '12', '13', '1', '2']
kidsL = ['10H', '11', '11H', '12', '12H', '13', '13H', '1', '1H', '2', '2H']
menswhole = ['9', '10', '11']
mens = ['8H', '9', '9H', '10', '10H', '11']
wmnswhole = ['6', '7', '8']
wmns = ['6H', '7', '7H', '8', '8H']

for i in range(len(df)):
    if df.at[i, 'Gender'] in ['BOYBOYS', 'GIRLGIRLS']:
        if df.at[i, 'L,N'] == 'L':
            if df.at[i, 'Whole Sizes Only vs Half and Whole'] == 'Whole Sizing':
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidswholeL) else ''
            else:
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidsL) else ''
        elif df.at[i, 'L,N'] == 'N':
            if df.at[i, 'Whole Sizes Only vs Half and Whole'] == 'Whole Sizing':
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidswholeN) else ''
            else:
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidsN) else ''
    elif df.at[i, 'Gender'] == 'MENMENS':
        if df.at[i, 'Whole Sizes Only vs Half and Whole'] == 'Whole Sizing':
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in menswhole) else ''
        else:
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in mens) else ''
    elif df.at[i, 'Gender'] == 'WMNWOMENS':
        if df.at[i, 'Whole Sizes Only vs Half and Whole'] == 'Whole Sizing':
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in wmnswhole) else ''
        else:
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in wmns) else ''


# In[9]:


df.to_excel('output_file.xlsx', index=False)


# In[ ]:




