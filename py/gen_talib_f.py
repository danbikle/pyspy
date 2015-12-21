# gen_talib_f.py

# Demo:
# cd     ~/ddata
# python ~/pyspy/py/gen_talib_f.py ftrGSPC2.csv

import pandas as pd
import numpy  as np
import talib
import pdb

# I should check cmd line arg
import sys

#  len(sys.argv) should == 2
if len(sys.argv) == 1:
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/pyspy/py/gen_talib_f.py ftrGSPC2.csv')
  print('...')
  sys.exit()

infile = sys.argv[1]
df1    = pd.read_csv(infile)
cp_a   = df1['cp'].values
output = talib.SMA(cp_a)

from talib import MA_Type
upper, middle, lower = talib.BBANDS(cp_a, matype=MA_Type.T3)

upper[ -4:]
middle[-4:]
lower[ -4:]

