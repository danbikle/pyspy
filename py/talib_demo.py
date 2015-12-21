# talib_demo.py

# Demo:
# cd     ~/pyspy/demodata
# python ~/pyspy/py/talib_demo.py ftrGSPC2.csv

import pandas as pd
import numpy  as np
import talib
import pdb

# I should check cmd line arg
import sys

#  len(sys.argv) should == 2
if len(sys.argv) == 1:
  print('Demo:')
  print('cd ~/pyspy/demodata')
  print('python ~/pyspy/py/talib_demo.py ftrGSPC2.csv')
  print('...')
  sys.exit()

infile = sys.argv[1]
df1    = pd.read_csv(infile)
cp_a   = df1['cp'].values

sma_a = talib.SMA(cp_a)
# help(talib.SMA)
# http://mrjbq7.github.io/ta-lib/func.html
# http://mrjbq7.github.io/ta-lib/func_groups/overlap_studies.html
# http://www.tadoc.org/indicator/SMA.htm

from talib import MA_Type
# Calculating bollinger bands, with triple exponential moving average:
upper_a, middle_a, lower_a = talib.BBANDS(cp_a, matype=MA_Type.T3)
# help(talib.BBANDS)
# help(MA_Type)
# http://www.google.com/search?q=in+technical+analysis+what+are+bollinger+bands
# http://www.tadoc.org/indicator/BBANDS.htm

mom_a = talib.MOM(cp_a, timeperiod=5)
# help(talib.MOM)
# http://www.google.com/search?q=in+technical+analysis+what+is+momentum+indicator
# http://www.tadoc.org/indicator/MOM.htm
# http://mrjbq7.github.io/ta-lib/func_groups/momentum_indicators.html
# Demo of abstract

from talib.abstract import *
# http://mrjbq7.github.io/ta-lib/abstract.html
sma_df = SMA(df1, timeperiod=25, price='cp')

'end'

