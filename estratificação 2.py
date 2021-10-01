# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:44:18 2021

@author: Jailson
"""

import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split



df = pd.read_csv('Amazon.csv')


train, test = train_test_split(df, test_size=0.1)

test1 = test.to_csv(sep = ',', header = True, index = False)

arquivo = open('train8.csv','a')
arquivo.write(test1)
arquivo.close()


teste = pd.read_csv('train8.csv')
teste = teste.dropna()



from sklearn.cross_validation import train_test_split


import numpy as np

import math

total_size=len(df)

train_size=math.floor(0.9*total_size)

#training dataset
train=df.head(train_size)
#test dataset
test=df.tail(len(df) -train_size)