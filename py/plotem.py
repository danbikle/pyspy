# plotem.py

# This script should plot data in a CSV file

# Demo:
# cd ~/ddata
# python ~/pyspy/py/plotem.py learn_test.csv

import pandas as pd
import numpy  as np
import pdb
import datetime

# I should check cmd line arg
import sys

print('hello, from '+ sys.argv[0])

#  len(sys.argv) should == 2
if len(sys.argv) == 1:
  print('I need a command line arg.')
  print('Demo:')
  print('python '+sys.argv[0]+' learn_test.csv')
  print('Try again. bye.')
  sys.exit()

csvf = sys.argv[1]
print(csvf)

# I should load the csv into a DataFrame
df1 = pd.read_csv(csvf)



pdb.set_trace()
'done'
