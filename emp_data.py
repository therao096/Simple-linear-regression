# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:40:13 2020

@author: Varun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
empdata= pd.read_csv("emp_data.csv")
empdata
empdata.columns
empdata.columns=['salary','churnoutrate']
empdata.columns
plt.hist(empdata.salary)
plt.boxplot(empdata.salary)
plt.boxplot(empdata.salary,0,"bs",0)
plt.plot(empdata.salary,empdata.churnoutrate,"rs"); plt.xlabel("salary"); plt.ylabel("churn out rate") ;
######coreelation
empdata.churnoutrate.corr(empdata.salary)
####model building
import statsmodels.formula.api as smf
model=smf.ols("churnoutrate~salary", data=empdata).fit()
model.params
model.summary()
model.conf_int(0.05)
pred=model.predict(empdata)
pred
plt.scatter(x=empdata['salary'],y=empdata['churnoutrate'],color='red');plt.plot(empdata['salary'],pred,color='black');plt.xlabel('salary');plt.ylabel('churnoutrate')
