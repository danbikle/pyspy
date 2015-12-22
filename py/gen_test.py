# gen_test.py

# This script should generate test data.

# Demo:
# cd ~/ddata
# python ~/pyspy/py/gen_test.py 2014 2016 ftr_wbb_ftrGSPC2.csv

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys

#  len(sys.argv) == 4 should be true
if len(sys.argv) < 4:
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/pyspy/py/gen_test.py  2014 2016 ftr_wbb_ftrGSPC2.csv')
  print('...')
  sys.exit()

yr1    = sys.argv[1]
yr2    = sys.argv[2]
infile = sys.argv[3]

# I should load the CSV into a DF.
df1 = pd.read_csv(infile)
# I should remove older data I do not want:
pred1 = df1['cdate']>yr1
df2   = df1[pred1]
# I should remove newer data which I will test with later:
pred2 = df2['cdate']<yr2
df3   = df2[pred2]
# I should write it to CSV
df3.to_csv('test.csv', float_format='%4.3f', index=False)
'done'
