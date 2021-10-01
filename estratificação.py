# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:35:11 2021

@author: Jailson
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

df = pd.read_csv('Amazon.csv', index_col=['Date'])

df.dtypes

df.isnull().sum()

df.head()

df.describe()

corr = df.corr()

corr

corr.shape

plt.figure(figsize=(6,6))
sns.heatmap(corr, cbar=True, square= True, fmt='.1f', annot=True, annot_kws={'size':15}, cmap='Greens')

df1 = df.drop(columns=['Volume'])

total_size=len(df)

train_size = math.floor(0.8*total_size)

#training dataset
train=df.head(train_size)
#test dataset
test=df.tail(len(df) -train_size)

test1 = test.to_csv(sep = ',', header = True, index = False)

arquivo = open('train9.csv','w')
arquivo.write(test1)
arquivo.close()

teste = pd.read_csv('train9.csv')



