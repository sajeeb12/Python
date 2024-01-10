# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:45:47 2021

@author: Sajeeb
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
data = pd.read_csv("input_2018-2-60-045.csv")
print(data)
#%%
x = data['x'].values
y = data['y'].values
print(x)
print(y)
#%%
plt.scatter(x,y,)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
#%%
def mean_2018_2_60_045(x):
    sum = 0
    for i in x:
        sum = sum+i
    return sum/len(x)
mean_x = mean_2018_2_60_045(x)
mean_y = mean_2018_2_60_045(y)
print(f"Mean of X: {mean_x}")
print(f"Mean of Y: {mean_y}")
#%%
def var_2018_2_60_045(x,mean_x):
    sum = 0
    for i in x:
        sum = sum + (i-mean_x)**2
    return sum/len(x)-1
var = var_2018_2_60_045(x,mean_x)
print(f'Variance: {var}')
#%%
def cov_2018_2_60_045(x, y, mean_of_x, mean_of_y):
    sum = 0
    for i in range(0, len(x)):
        sum = sum + (x[i]-mean_of_x)*(y[i]-mean_of_y)
    return sum/(len(x)-1)
cov = cov_2018_2_60_045(x,y,mean_x,mean_y)
print(f"Covariance: {cov}")
#%%
b = cov/var
print(b)
#%%
a = mean_y-(b*mean_x)
print(a)
#%%
y1 = a+b*x
print(y1)
#%%
def sse_2018_2_60_045(y,y1):
    sum = 0
    for i in range(0,len(y)):
        sum =sum+(y1[i]-y[i])**2
    return sum
sse = sse_2018_2_60_045(y, y1)
print(sse)
#%%
plt.scatter(x,y1)
z = np.polyfit(x, y1, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()







   