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
upper_a, middle_a, lower_a = talib.BBANDS(cp_a)

# I should widen df before output
df1['upf']  = list(upper_a / cp_a)
df1['lowf'] = list(cp_a / lower_a)
pdb.set_trace()
df1.head()
df1.tail()
'done'
