# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:08:20 2024

@author: munis
"""
#Value Inc is a retail store that sells household items all over the world by bulk.

#The Sales Manager has no sales reporting but he has a brief idea of current sales.
#He also has no idea of the monthly cost, profit and top selling products. He wants a
#dashboard on this and says the data is currently stored in an excel sheet

import pandas as pd

#importing data into python
data = pd.read_csv('transactions.csv', sep=';')

#getting a look at the data
data.head()
data.info()  

#Merging all the days, month and year to create a date column for easy access
#Converting int values into str
data['Day'].astype(str)
data['Year'].astype(str)
data['Date'] = data['Day'].astype(str)+'-'+data['Month']+'-'+data['Year'].astype(str)

#Making some calculations for overall profit
#Calculating the overall seliing price 
data['OverallSellingPrice'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#Calculating the overall cost price
data['OverallCostPrice'] = data['CostPerItem']*data['NumberOfItemsPurchased']

#Calculating the profit and markup
data['OverallProfit'] = data['OverallSellingPrice'] - data['OverallCostPrice']
data['Markup'] = data['OverallProfit'] / data['OverallCostPrice']
#Rounding up the decimals
data['Markup'] = round(data['Markup'], 2)

#Merging CSV files
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')
data = pd.merge(data, seasons, on='Month' )

#Cleaning our data for a more effective use
split_col = data['ClientKeywords'].str.split(',', expand=True)
 
#Creating new columns after the split
data['AgeRange'] = split_col[0]
data['ClietType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

data['AgeRange'] = data['AgeRange'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#Dropping unnecessary columns
data = data.drop('ClientKeywords', axis=1)
data = data.drop(['Day', 'Month', 'Year'], axis=1)

#Exporting our CSV
data.to_csv('Value_Inc_Cleaned.csv', index=False)













































            