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

pdb.set_trace()
trainf = sys.argv[1]
testf  = sys.argv[2]

