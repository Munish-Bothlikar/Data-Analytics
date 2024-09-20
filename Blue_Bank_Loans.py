# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:18:53 2024

@author: munis
"""
#Blue Bank is a bank in USA that has a loan department which is currently understaffed.
#They supply loans to individuals and don’t have much reporting on how risky these
#borrowers are.

#Using Python and Tableau, they’d like to see a report of borrowers who may have
#issues paying back the loan.

#Importing libraries
import pandas as pd
import numpy as np
import json

#Reading the JSON file
json_file = open('loan_data_json.json')
loan_data = json.load(json_file)

#Getting data into a dataFrame
data = pd.DataFrame(loan_data)

#Getting some info
data.head()
data.info()
data.describe()

#Cleaning the data
#Rounding off some data fields
data['int.rate'] = round(data['int.rate'], 2)
data['days.with.cr.line'] = round(data['days.with.cr.line'], 0)
data['revol.util'] = round(data['revol.util'], 0)

#Finding annual income
data['annual.inc'] = np.exp(data['log.annual.inc'])
data = data.drop('log.annual.inc', axis = 1)
data['annual.inc'] = round(data['annual.inc'], 0)
  
#FICO: The FICO credit score of the borrower.
# 300 - 400: Very Poor
# 401 - 600: Poor
# 601 - 660: Fair
# 661 - 780: Good
# 781 - 850: Excellent

ficocat = []
for i in range(0, len(data)):
    score = data['fico'][i]
    if score in range(300, 400):
        cat = 'Very Poor'
    elif score in range(401, 600):
        cat = 'Poor'
    elif score in range(601, 660):
        cat = 'Fair'
    elif score in range(661, 780):
        cat = 'Good'
    elif score in range(781, 850):
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
data['fico.category'] = ficocat
#Personal note: Grasped the concepts of 'if' and 'for' loops
#Getting all the values in a newly created string and then creating a new column
#in DataFrame to accomodate that string

#Above categorization can also be done by 'loc' function
data.loc[data['int.rate']> 0.12, 'int.rate.type'] = 'High'
data.loc[data['int.rate']<= 0.12, 'int.rate.type'] = 'Low'

#Exporting to CSV
data.to_csv('Blue_Bank_Cleaned.csv', index = True)



























