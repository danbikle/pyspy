# gen_train.py

# This script should generate training data.

# Demo:
# cd ~/ddata
# python ~/pyspy/py/gen_train.py 25 ftr_wbb_ftrGSPC2.csv

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys
pdb.set_trace()

#  len(sys.argv) == 3 should be true
if len(sys.argv) < 3:
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/pyspy/py/gen_train.py 25 ftr_wbb_ftrGSPC2.csv')
  print('...')
  sys.exit()

yr_i   = int(sys.argv[1])
infile = sys.argv[2]

# I should load the csv into a DF.

df1  = pd.read_csv(infile)
