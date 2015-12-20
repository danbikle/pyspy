# ~/pyspy/py/genf.py

# This script should generate features from prices

# Demo:
# cd ~/ddata
# python ~/pyspy/py/genf.py GSPC2.csv

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys

print('hello, from '+ sys.argv[0])

#  len(sys.argv) should == 2
if len(sys.argv) == 1:
  print('Demo:')
  print('cd ~/ddata')
  print('python python ~/pyspy/py/genf.py GSPC2.csv')
  print('...')
  sys.exit()

infile = sys.argv[1]
print('I am building features from this file:')
print(infile)
print('Busy...')

df1  = pd.read_csv(infile)
df1.columns = ['cdate','cp']

cp_a = df1[['cp']].values
# cp should be a list:
cp   = [elm[0] for elm in cp_a]

cplead_l = [cp[0]] + cp
cplag1_l = cp +     [cp[-1]]
cplag2_l = cp +     [cp[-1]] + [cp[-1]]
cplag4_l = cp +     [cp[-1]] + [cp[-1]] + [cp[-1]] + [cp[-1]]
cplag8_l = cplag4_l + [cp[-1]] + [cp[-1]] + [cp[-1]] + [cp[-1]]
# I should snip off ends so new columns as long as cp:
cplead_l = cplead_l[:-1]
cplag1_l = cplag1_l[1:]
cplag2_l = cplag2_l[2:]
cplag4_l = cplag4_l[4:]
cplag8_l = cplag8_l[8:]

# NumPy allows me to do arithmetic on its Arrays.
# I should convert my lists to Arrays:
cp_a     = np.array(cp)
cplead_a = np.array(cplead_l)
cplag1_a = np.array(cplag1_l)
cplag2_a = np.array(cplag2_l)
cplag4_a = np.array(cplag4_l)
cplag8_a = np.array(cplag8_l)

# I should calculate pct-deltas:
pctlead_a = 100.0 * (cplead_a - cp_a)/cp_a
pctlag1_a = 100.0 * (cp_a - cplag1_a)/cplag1_a
pctlag2_a = 100.0 * (cp_a - cplag2_a)/cplag2_a
pctlag4_a = 100.0 * (cp_a - cplag4_a)/cplag4_a
pctlag8_a = 100.0 * (cp_a - cplag8_a)/cplag8_a

# I am done doing calculations.
# I should put my 5 new columns into my DataFrame.

df1['pctlead'] = pctlead_a
df1['pctlag1'] = pctlag1_a
df1['pctlag2'] = pctlag2_a
df1['pctlag4'] = pctlag4_a
df1['pctlag8'] = pctlag8_a

# I should save my work into a CSV file.
# My input file should look something like this:
# GSPC2.csv
# I should save my work as something like this:
# ftrGSPC2.csv
df1.to_csv('ftr'+infile, float_format='%4.3f', index=False)
print('The features are in this file:')
print('ftr'+infile)
print('Now the machine can learn.')

# done
