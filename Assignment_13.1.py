
# coding: utf-8

# In[58]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

'''Some values in the the FlightNumber column are missing. These numbers are meant
to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
these missing numbers and make the column an integer column (instead of a float
column).'''


df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)

'''The From_To column would be better as two separate columns! Split each string on
the underscore delimiter _ to give a new temporary DataFrame with the correct values.
Assign the correct column names to this temporary DataFrame.'''


dftemp = pd.DataFrame(df.From_To.str.split('_').tolist(),
                                   columns = ['From','To'])


'''Notice how the capitalisation of the city names is all mixed up in this temporary
DataFrame. Standardise the strings so that only the first letter is uppercase (e.g.
"londON" should become "London".)'''

dftemp['From']=dftemp.From.str.title()
dftemp['To']=dftemp.To.str.title()
dftemp

'''Delete the From_To column from df and attach the temporary DataFrame from the
previous questions.'''

df.drop('From_To', axis=1, inplace=True)
df=df.join(dftemp)
df

'''In the RecentDelays column, the values have been entered into the DataFrame as a
 list. We would like each first value in its own column, each second value in its own
column, and so on. If there isn't an Nth value, the value should be NaN.'''

dfdelay=df['RecentDelays'].apply(lambda row: pd.Series(row))
dfdelay.columns=['Delay1','Delay2','Delay3']
dfdelay

'''Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
delay_2, etc. and replace the unwanted RecentDelays column in df with delays.'''

df.drop('RecentDelays', axis=1, inplace=True)
dfnew=df.join(dfdelay)
dfnew


# In[41]:


dftemp = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
dftemp = pd.DataFrame(dftemp.From_To.str.split('_').tolist(),
                                   columns = ['country1','country2'])
dftemp
dftemp['country1']=dftemp.country1.str.title()
dftemp['country2']=dftemp.country2.str.title()
dftemp

