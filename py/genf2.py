# genf2.py

# Demo:
# cd     ~/ddata
# python ~/pyspy/py/genf2.py GSPC2.csv

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
  print('python python ~/pyspy/py/genf2.py GSPC2.csv')
  print('...')
  sys.exit()

infile      = sys.argv[1]
df1         = pd.read_csv(infile)
df1.columns = ['cdate','cp']
cp_a        = df1[['cp']].values
output      = talib.SMA(cp_a)
