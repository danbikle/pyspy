# talib_demo.py

# Demo:
# cd     ~/pyspy/demodata
# python ~/pyspy/py/talib_demo.py ftrGSPC2.csv
# http://www.tadoc.org/index.htm

import pandas as pd
import numpy  as np
import talib
import pdb

# I should check cmd line arg
import sys

df1     = pd.read_csv('ftrGSPC2.csv')
cdate_l = list(df1['cdate'].values)
cp_a    = df1['cp'].values

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
sma2_sr = abstract.SMA(df1, timeperiod=25, price='cp')
sma2_df = pd.DataFrame(df1['cdate'])
sma2_df['sma'] = list(sma2_sr)
# I should write Simple Moving Avg to file
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
# I should write Bollinger Bands to file
df3.to_csv('/tmp/bbands1.csv', float_format='%4.3f', index=False)

# Demos of Momentum Indicators
# http://mrjbq7.github.io/ta-lib/func_groups/momentum_indicators.html

df1     = pd.read_csv('ftrGSPC2.csv')
cdate_l = list(df1['cdate'].values)
cp_a    = df1['cp'].values

# http://www.tadoc.org/indicator/APO.htm
apo_a = talib.APO(cp_a, fastperiod=12, slowperiod=26, matype=0)

# http://www.tadoc.org/indicator/CMO.htm
cmo_a = talib.CMO(cp_a, timeperiod=14)

# http://www.tadoc.org/indicator/MACD.htm
macd_a, macdsignal_a, macdhist_a = talib.MACD(cp_a, fastperiod=12, slowperiod=26, signalperiod=9)

# http://www.tadoc.org/indicator/ROC.htm
roc_a = talib.ROC(cp_a, timeperiod=10)

# http://www.tadoc.org/indicator/RSI.htm
rsi_a = talib.RSI(cp_a, timeperiod=14)

# Demo of cycle indicators
# http://mrjbq7.github.io/ta-lib/func_groups/cycle_indicators.html

# http://www.tadoc.org/indicator/HT_PHASOR.htm
inphase_a, quadrature_a = talib.HT_PHASOR(cp_a)
pdb.set_trace()

'end'
