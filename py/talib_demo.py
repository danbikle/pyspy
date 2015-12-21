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

df1    = pd.read_csv('ftrGSPC2.csv')
cp_a   = df1['cp'].values

sma_a  = talib.SMA(cp_a)

# help(talib.SMA)
# http://mrjbq7.github.io/ta-lib/func.html
# http://mrjbq7.github.io/ta-lib/func_groups/overlap_studies.html
# http://www.tadoc.org/indicator/SMA.htm

# For convenience, the Function API supports both numpy.ndarray and pandas.Series types?
# sma_df = talib.SMA(df1['cp'])
# *** TypeError: Argument 'real' has incorrect type (expected numpy.ndarray, got Series)
# talib.SMA() supports only numpy.ndarray

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

# demos using abstract API:

from talib import abstract

# http://mrjbq7.github.io/ta-lib/abstract.html

# Notice that first param is my dataframe named df1:

sma2_df = abstract.SMA(df1, timeperiod=25, price='cp')
sma2_df.to_csv('/tmp/sma2.csv', float_format='%4.3f', index=False)

# help(abstract.BBANDS)
# Here is a demo of abstract.BBANDS

df2 = pd.read_csv('GSPC.csv')
cdate_l  = list(reversed(df2['Date'  ].values))
open_l   = list(reversed(df2['Open'  ].values))
high_l   = list(reversed(df2['High'  ].values))
low_l    = list(reversed(df2['Low'   ].values))
close_l  = list(reversed(df2['Close' ].values))
volume_l = list(reversed(df2['Volume'].values))

input_arrays = {}
input_arrays['open']   = np.array(open_l)
input_arrays['high']   = np.array(high_l)
input_arrays['low']    = np.array(low_l)
input_arrays['close']  = np.array(close_l)
input_arrays['volume'] = np.array(volume_l)
upperband_a, middleband_a, lowerband_a = abstract.BBANDS(input_arrays, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

df3 = pd.DataFrame(cdate_l)
df3.columns = ['cdate']

df3['close']  = close_l
df3['upperband']  = list(upperband_a)
df3['middleband'] = list(middleband_a)
df3['lowerband']  = list(lowerband_a)
df3.to_csv('/tmp/bbands1.csv', float_format='%4.3f', index=False)
'end'
