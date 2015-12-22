# ~/pyspy/py/genf_talib.py

# This script should generate features from prices

# Demo:
# cd ~/ddata
# python ~/pyspy/py/genf_talib.py ftrGSPC2.csv

import pandas as pd
import numpy  as np
import talib
import pdb

# I should check cmd line arg
import sys

print('hello, from '+ sys.argv[0])

#  len(sys.argv) should == 2
if len(sys.argv) == 1:
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/pyspy/py/genf_talib.py ftrGSPC2.csv')
  print('...')
  sys.exit()

infile = sys.argv[1]
print('I am building features from this file:')
print(infile)
print('Busy...')

df1  = pd.read_csv(infile)



# I should pull cp out of the df
cp_a    = df1['cp'].values

# I should calculate Bollinger Bands

upper_a, middle_a, lower_a = talib.BBANDS(cp_a,timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

# I should widen df before output
df1['upf']  = list(upper_a / cp_a)
df1['lowf'] = list(cp_a / lower_a)
df1.to_csv('ftr_wbb_'+infile, float_format='%4.3f', index=False)

# I am done now but while I have the data available,
# let us look at upf and lowf.
# We start by asking,
# What is avg pctlead?
pctlead_a      = df1['pctlead'].values
pctlead_avg    = np.mean(pctlead_a)
pctlead_median = np.median(pctlead_a)

# I should get high relative price
pred_cphi      = df1['upf'] < 1.001
cphi_df        = df1[['cdate','pctlead']][pred_cphi]
len(cphi_df)
# If I have high relative price,
# what happens to pctlead?
pctlead_cphi_a      = cphi_df['pctlead'].values
pctlead_cphi_avg    = np.mean(pctlead_cphi_a)
pctlead_cphi_median = np.median(pctlead_cphi_a)

# Are these lower or higher than pctlead_avg pctlead_median?
pctlead_cphi_avg
pctlead_cphi_median

# I should get low relative price
pred_cplow      = df1['lowf'] < 1.001
cplow_df        = df1[['cdate','pctlead']][pred_cplow]
len(cplow_df)
# If I have low relative price,
# what happens to pctlead?
pctlead_cplow_a      = cplow_df['pctlead'].values
pctlead_cplow_avg    = np.mean(pctlead_cplow_a)
pctlead_cplow_median = np.median(pctlead_cplow_a)

# Are these lower or higher than pctlead_avg pctlead_median?
pctlead_cplow_avg
pctlead_cplow_median

# Perhaps pctlead depends on pctlead_cphi, pctlead_cplow

'done'
