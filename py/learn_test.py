# learn_test.py

# This script should learn and then test.

# Demo:
# cd ~/ddata
# python ~/pyspy/py/learn_test.py training.csv test.csv

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys

#  len(sys.argv) == 3 should be true
if len(sys.argv) < 3:
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/pyspy/py/learn_test.py training.csv test.csv')
  print('...')
  sys.exit()

trainf = sys.argv[1]
testf  = sys.argv[2]

# I should load the CSV files
train_df = pd.read_csv(trainf)
test_df  = pd.read_csv(testf)
train_a = np.array(train_df)
test_a  = np.array(test_df)

# I should declare some integers to help me navigate the Arrays.
pdb.set_trace()
cdate_i   = 0
cp_i      = 1
pctlead_i = 2
pctlag1_i = 3
pctlag2_i = 4
pctlag4_i = 5
pctlag8_i = 6
upf_i     = 7
lowf_i    = 8

