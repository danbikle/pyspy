# ~/pyspy/py/genf_talib.py

# This script should generate features from prices

# Demo:
# cd ~/ddata
# python ~/pyspy/py/genf_talib.py ftrGSPC2.csv

import pandas as pd
import numpy  as np
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

pdb.set_trace()
df1.columns
df1.tail()
