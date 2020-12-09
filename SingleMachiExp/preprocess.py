#!/usr/bin/env python
# coding: utf-8

# In[11]:


## this will create columns for mean and count for each unique values in all columns
import pandas as pd
def preprocess(data):
    for col in data.columns[1:]:
        means = data.groupby(col)['col1'].mean()
        mean_dict = means.to_dict()

        counts = data.groupby(col)['col1'].count()
        count_dict = counts.to_dict()

        mean_column = col + '_mean'
        count_column = col + "_count"

        data[mean_column] = data[col].map(mean_dict,na_action='ignore')
        data[count_column] = data[col].map(count_dict,na_action='ignore')
        
def main():
    columns = ['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10',
           'col11','col12','col13','col14','col15','col16','col17','col18','col19','col20',
          'col21','col22','col23','col24','col25','col26','col27','col28','col29','col30',
          'col31','col32','col33','col34','col35','col36','col37','col38','col39','col40']
    i=1
    for data in pd.read_csv("train.txt.zip",skiprows = 5000000 ,chunksize=5000000, delimiter="\t" ,header=None, compression="zip"):
        data.columns = columns
        data.to_csv("chunk" + str(i) + ".txt")
        i = i + 1
        break
    data=data.drop(columns=["Unnamed: 0"])
    preprocess(data)
    data = data.drop(columns=columns[1:])
    data=data.drop(columns = [ 'col1_mean_mean', 'col1_mean_count'])
    data.to_csv("preprocessed.csv.gz", compression="gzip")


# In[ ]:




