# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:43:17 2021

@author: Jailson
"""

import pandas as pd

df_price = pd.read_csv('train.csv')

base = df_price.loc[:,['OverallQual','YearBuilt','YearRemodAdd', 'TotalBsmtSF','1stFlrSF',
'GrLivArea','FullBath','TotRmsAbvGrd','GarageCars','GarageArea','SalePrice',]]

df_price['GrLivArea'].describe()

df_price.info()

df_price(columns = ['LotFrontage', 'Alley', 'MasVnrArea', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 
                         'BsmtFinType1','FireplaceQu', 'BsmtFinType2',  'GarageType', 'GarageYrBlt', 'GarageFinish', 
                         'GarageQual', 'GarageCond', 'PoolQC', 'Fence', 'MiscFeature'])

df_price.drop(df_price[df_price['Electrical'].isnull()].index, inplace= True)

import seaborn as sns
import matplotlib.pyplot as plt

corr = df_price.corr(method = 'pearson')
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corr, vmax=1, square=True);
corr = corr.loc['SalePrice':, :].T
corr = corr[(corr['SalePrice'] >0.5) | (corr['SalePrice'] < -0.5)]
corr


df_price.drop(df_price[df_price['GrLivArea'] > 4000].index, inplace = True)
df_price.drop(df_price[df_price['TotalBsmtSF'] > 3000].index, inplace = True)
df_price.drop(df_price[df_price['1stFlrSF'] > 2800].index, inplace = True)


plt.plot(df_price['TotalBsmtSF'], color = 'blue')
plt.show()


sns.set(style="whitegrid", color_codes=True)
sns.boxplot(df_price['1stFlrSF']);


from pandas.api.types import is_numeric_dtype
import category_encoders as ce
from sklearn.preprocessing import LabelEncoder

num = []
categ = []
for row in df_price.columns: 
    numeric = is_numeric_dtype(df_price[row])
    if row not in num and numeric == False:
        categ.append(row)
    elif row not in categ and numeric == True:
        num.append(row)
        
        
for row in categ:
    
    ce_ord = ce.OrdinalEncoder(cols=[row])
    df_price[row] = ce_ord.fit_transform(df_price[row], df_price['SalePrice'])
for row in categ:
    var = row
    plt.figure()
    plt.scatter(df_price[var],df_price['SalePrice'])
    plt.xlabel(var), plt.ylabel('SalePrice')
corr_all = df_price.corr(method = 'pearson')
corr_all = corr_all.loc['SalePrice':, :].T
corr_all = corr_all[(corr_all['SalePrice'] >0.5) | (corr_all['SalePrice'] < -0.5)]
corr_all

corr1 = corr_all.merge(corr, left_index = True, right_index = True, how= 'outer')
corr1
        
train_df = pd.DataFrame(df_price, columns = corr.index)

SalePrice = train_df.pop('SalePrice')

base = train_df.cat(Saleprice,sep=" ")
base = train_df.apply(SalePrice, axis=1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        