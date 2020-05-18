# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:02:55 2020

@author: Varun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
calorie= pd.read_csv("calories_consumed.csv")
calorie.columns
calorie.columns=['weight','calories']
plt.hist( calorie.calories )
plt.boxplot(calorie.calories)
plt.boxplot(calorie.calories,0,"bs",0)
plt.plot(calorie.calories,calorie.weight,"ro");plt.xlabel("calories");plt.ylabel("weight")

np.corrcoef(calorie['Weight gained (grams)'],calorie['Calories Consumed'])
calorie.weight.corr(calorie.calories )
###strong corelation
import statsmodels.formula.api as smf
model=smf.ols("weight~calories", data=calorie).fit()
model.params
model.summary()
model.conf_int(0.05)
pred=model.predict(calorie)
pred
import matplotlib.pylab as plt
plt.scatter(x=calorie['calories'],y=calorie['weight'],color='red');plt.plot(calorie['calories'],pred,color='black');plt.xlabel('calories');plt.ylabel('weight')
