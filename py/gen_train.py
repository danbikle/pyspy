# gen_train.py

# This script should generate training data.

# Demo:
# cd ~/ddata
# python ~/pyspy/py/gen_train.py 1987 2014 ftr_wbb_ftrGSPC2.csv

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys
pdb.set_trace()

#  len(sys.argv) == 4 should be true
if len(sys.argv) < 4:
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/pyspy/py/gen_train.py 25 ftr_wbb_ftrGSPC2.csv')
  print('...')
  sys.exit()

yr1    = int(sys.argv[1])
yr2    = int(sys.argv[2])
infile =     sys.argv[3]

# I should load the csv into a DF.
pdb.set_trace()
df1 = pd.read_csv(infile)
df2 = df1['cdate'>yr1]
df3 = df2['cdate'<yr2]
