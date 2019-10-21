
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
# read in data
monthly = pd.read_csv('monthly_sales.csv')
daily = pd.read_csv('daily_sales.csv')
monthly.set_index('Month, Year',inplace=True)

#Filter monthly data
monthly_filtered = monthly.iloc[24:]

# Create CSVs with Data from each region and each food 
hamburger_cols = ['HM-NE','HM-NW','HM-C','HM-SW','HM-SE']
chicken_cols = ['CF-NE','CF-NW','CF-C','CF-SW','CF-SE']
fish_cols = ['FF-NE','FF-NW','FF-C','FF-SW','FF-SE']
north_east_cols = ['FF-NE','HM-NE','CF-NE']
north_west_cols = ['FF-NW','HM-NW','CF-NW']
south_east_cols = ['FF-SE','HM-SE','CF-SE']
south_west_cols = ['FF-SW','HM-SW','CF-SW']
central_cols = ['FF-C','HM-C','CF-C']
hamburger_df = monthly_filtered[hamburger_cols]
hamburger_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/Hamburgers.csv')
chickens_df = monthly_filtered[chicken_cols]
chickens_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/Chickens.csv')
fish_df = monthly_filtered[fish_cols]
fish_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/Fish.csv')
NE_df = monthly_filtered[north_east_cols]
NE_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/NE.csv')
NW_df = monthly_filtered[north_west_cols]
NW_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/NW.csv')
SE_df = monthly_filtered[south_east_cols]
SE_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/SE.csv')
SW_df = monthly_filtered[south_west_cols]
SW_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/SW.csv')
Central_df = monthly_filtered[central_cols]
Central_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/Central.csv')

#Create CSV with sales by food 
sales_hamburgers = hamburger_df.iloc[8:10].sum(axis=1).to_frame().rename({0:'Burger Sales'},axis=1)
sales_hamburgers.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/burger_sales.csv')
sales_chicken = chickens_df.iloc[8:10].sum(axis=1).to_frame().rename({0:'Chicken Sales'},axis=1)
sales_chicken.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/chicken_sales.csv')
sales_fish = fish_df.iloc[8:10].sum(axis=1).to_frame().rename({0:'Fish Sales'},axis=1)
sales_fish.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/fish_sales.csv')
sales_df.to_csv('/Users/jaredandrews/Applications/DSC106/DSC106HW2/sales_region.csv')

