#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd





df = pd.read_excel('01.15.2024 Ship.xlsx')


# In[21]:


df.info()


# In[22]:


columns_to_fill = ['3', '3H', '4', '4H', '5', '5H', '6', '6H', '7', '7H', '8', '8H', '9', '9H', '10', '10H', '11', '11H', '12', '12H', '13', '13H', '1', '1H', '14', '2', '2H', '15', '16']

df[columns_to_fill].fillna(0, inplace=True)


# In[23]:


#need to create (1) L,N column and Whole Sizes Only vs Half and Whole
#L,N Column
df['L,N'] = df['Style'].astype(str).str[-1]


# In[24]:


# #identify if a SKU is whole sizes or not
# kidsL = ['10H', '11', '11H', '12', '12H', '13', '13H', '1', '1H', '2', '2H']
# kidsN = ['5', '5H', '6', '6H', '7', '7H', '8', '8H', '9', '9H', '10']
# mens = ['8H', '9', '9H', '10', '10H', '11']
# wmns = ['6H', '7', '7H', '8', '8H']


# for i in range(len(df)):
#     if df.at[i, 'Gender'] in ['BOYBOYS', 'GIRLGIRLS']:
#         if df.at[i, 'L,N'] == 'L':
#             sizes_ending_in_H = [size for size in kidsL if size.endswith('H')]
            
#             if all(df.at[i, size] == 0 for size in sizes_ending_in_H):
#                 df.at[i, 'Whole'] = 'Whole'
#         elif df.at[i, 'N,N'] == 'N':
#             N_sizes_ending_in_H = [size for size in kidsN if size.endswtih('H')]
            
#             if all(df.at[i, size]==0 for size in N_sizes_ending_in_H):
#                 df.at[i, 'Whole'] = 'Whole'
#     elif df.at[i, 'Gender'] == 'MENMENS':
#         MEN_sizes_ending_in_H = [size for size in mens if size.endswith('H')]
        
#         if all (df.at[i, size]==0 doe aiw in MEN_sizes_ending_in_H):
#             df.at[i, 'Whole'] = 'Whole'
            
#     elif df.at[i, 'Gender'] == 'WMNWOMENS':
#         WMN_sizes_ending_in_H = [size for size in wmns if size.endswith('H')]
        
#         if all (df.at[i, size]==0 doe aiw in WMN_sizes_ending_in_H):
#             df.at[i, 'Whole'] = 'Whole'
    

        

                


# In[25]:


kidsLhalf = ['10H','11H', '12H', '13H', '1H', '2H']
kidsNhalf = ['5H', '6H', '7H', '8H', '9H']
menshalf = ['8H', '9H', '10H']
wmnshalf = ['6H', '7H', '8H']

df['Whole'] = ""
# for every row
# first look at what kind of sku it is looking at 'Gender' and 'L,N' column
# depending on what kind of sku it is, we look up to a different list
# if the sum of those entries in the list, which are the half sizes are 0, then it is a whole size

for i in range(len(df)):
    if df.at[i, 'Gender'] in ['BOYBOYS', 'GIRLGIRLS']:
        if df.at[i, 'L,N'] == 'L':            
            if sum(df.at[i, col] for col in kidsLhalf) == 0:
                df.at[i, 'Whole'] = 'Whole'
        elif df.at[i, 'L,N'] == 'N':
            if sum(df.at[i, col] for col in kidsNhalf) == 0:
                df.at[i, 'Whole'] = 'Whole'
    elif df.at[i, 'Gender'] == 'MENMENS':
        if sum(df.at[i, col] for col in menshalf) == 0:
            df.at[i, 'Whole'] = 'Whole'
            
    elif df.at[i, 'Gender'] == 'WMNWOMENS':
        if sum(df.at[i, col] for col in wmnshalf) == 0:
            df.at[i, 'Whole'] = 'Whole'


# In[26]:


df['Whole'].unique()


# In[27]:


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
            if df.at[i, 'Whole'] == 'Whole':
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidswholeL) else ''
            else:
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidsL) else ''
        elif df.at[i, 'L,N'] == 'N':
            if df.at[i, 'Whole'] == 'Whole':
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidswholeN) else ''
            else:
                df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in kidsN) else ''
    elif df.at[i, 'Gender'] == 'MENMENS':
        if df.at[i, 'Whole'] == 'Whole':
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in menswhole) else ''
        else:
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in mens) else ''
    elif df.at[i, 'Gender'] == 'WMNWOMENS':
        if df.at[i, 'Whole'] == 'Whole':
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in wmnswhole) else ''
        else:
            df.at[i, 'Status'] = 'broken' if any(df.at[i, col] == 0 or pd.isnull(df.at[i, col]) for col in wmns) else ''




# In[28]:


#export

df.to_excel('output_file.xlsx', index=False)


# In[ ]:




