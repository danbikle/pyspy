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

# matplotlib likes dates:
cdate_l = [datetime.datetime.strptime(row, "%Y-%m-%d") for row in df1['cdate'].values]
# I should get values for y-axis now:
cp_l = [row for row in df1['cp']       ] 
gl_l = [row for row in df1['greenline']] 

# I should plot
import matplotlib
# http://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear
matplotlib.use('Agg')
# Order is important here.
# Do not move the next import:
import matplotlib.pyplot as plt
plt.plot(cdate_l, cp_l, 'b-', cdate_l, gl_l, 'g-')
pngf = csvf.replace('.csv','')+'.png'
plt.savefig(pngf)
plt.close()
print('New png file: ')
print(pngf)
'done'

