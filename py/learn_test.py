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
cdate_i   = 0
cp_i      = 1
pctlead_i = 2
pctlag1_i = 3
pctlag2_i = 4
pctlag4_i = 5
pctlag8_i = 6
upf_i     = 7
lowf_i    = 8
end_i     = 9
# I should build X-arrays (I call this 'independent' data).
x_train_a = train_a[:,pctlag1_i:end_i]
x_test_a  =  test_a[:,pctlag1_i:end_i]
# I should build y-arrays (I call this 'dependent' data, I assume y depends on X).
y_train_a = train_a[:,pctlead_i]
y_test_a  =  test_a[:,pctlead_i]
train_median  = np.median(y_train_a)
label_train_a = y_train_a > train_median
label_test_a  = y_test_a  > train_median

# Ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

from sklearn import linear_model
lrmodel = linear_model.LogisticRegression()
# I should use training data to train, also called 'fit' my lrmodel:
lrmodel.fit(x_train_a, label_train_a)
# Now that I have a model which has learned from x_train_a, label_train_a,
# I will use it to generate predictions from x_test_a
predictions_l = []
for xoos_a in x_test_a:
  xf_a        = xoos_a.astype(float)
  xr_a        = xf_a.reshape(1, -1)
  aprediction = lrmodel.predict_proba(xr_a)[0,1]
  predictions_l.append(aprediction)
len(test_df)         == len(predictions_l) # should be true
# I should match the predictions to the test observations.
test_df['prediction'] =     predictions_l
# I should capture prediction 'direction'. Above 0.5 is bullish else bearish.
test_df['pdir'] = [np.sign(prediction-0.5) for prediction in predictions_l]
# I should capture lead-price-deltas to help with later visualization.
cp_l = list(test_df['cp'].values)
lead_l = cp_l[1:] + [cp_l[len(cp_l)-1]]
len(cp_l)             == len(lead_l)           # should be true
lead_l[len(lead_l)-1] == lead_l[len(lead_l)-2] # should be true
lead_a = np.array(lead_l) - np.array(cp_l)
test_df['lead_delta'] = list(lead_a)
test_df['actual_dir'] = [np.sign(lead_delta) for lead_delta in lead_a]

# I should count positive predictions.
posp_df  = test_df[['pdir','actual_dir']][test_df['pdir'] == 1]
# I should count true positive predictions.
tposp_df = posp_df[posp_df['actual_dir'] == 1]
# I should calculate positive accuracy.
pos_acc  = 100.0 * len(tposp_df)/len(posp_df)

# I should count negative predictions.
negp_df  = test_df[['pdir','actual_dir']][test_df['pdir'] == -1]
# I should count true negative predictions.
tnegp_df = negp_df[negp_df['actual_dir'] == -1]
# I should calculate negative accuracy.
neg_acc  = 100.0 * len(tnegp_df)/len(negp_df)

# I should calculate combined accuracy
com_acc  = 100.0 * (len(tposp_df)+len(tnegp_df))/len(test_df)

# I should calculate 'effectiveness'.
pos_pctlead_a = np.array(test_df[['pctlead']][test_df['pdir'] == 1])
pos_eff       = np.mean(pos_pctlead_a)
neg_pctlead_a = np.array(test_df[['pctlead']][test_df['pdir'] == -1])
neg_eff       = np.mean(neg_pctlead_a)
longonly_eff  = np.mean(test_df['pctlead'].values)
# I should report
print('True  positive count: '+str(len(tposp_df)))
print('False positive count: '+str(len(posp_df)-len(tposp_df)))
print('True  negative count: '+str(len(tnegp_df)))
print('False negative count: '+str(len(negp_df)-len(tnegp_df)))

print('Accuracy of positive predictions: ' +str(pos_acc)[:6]+'%')
print('Accuracy of negative predictions: ' +str(neg_acc)[:6]+'%')
print('Combined Accuracy of predictions: ' +str(com_acc)[:6]+'%')
print('Positive Effectiveness: '  +str(pos_eff)[:6]+'%')
print('Negative Effectiveness: '  +str(neg_eff)[:6]+'%')
print('Long Only Effectiveness: ' +str(longonly_eff)[:6]+'%')

'done'

