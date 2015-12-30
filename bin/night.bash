#!/bin/bash

# ~/pyspy/bin/night.bash

# I should run this at night after daily closing price has been published.

# Demo:
# ~/pyspy/bin/night.bash
. ${HOME}/pyspy/pyspy_env.bash
# I should get prices and most recent price:
${PYSPY}/bin/wgetGSPCnight.bash

# I should generate features from prices:
cd $DDATA
python ${PYSPY}/py/genf.py       GSPC2.csv
python ${PYSPY}/py/genf_talib.py ftrGSPC2.csv
# I should generate training data from features.
python ${PYSPY}/py/gen_train.py 1987 2015 ftr_wbb_ftrGSPC2.csv
# I should generate test     data from features.
python ${PYSPY}/py/gen_test.py  2015 2016 ftr_wbb_ftrGSPC2.csv
# I should learn then test
python ${PYSPY}/py/learn_test.py training.csv test.csv
# I should visualize the predictions:
python ${PYSPY}/py/plotem.py learn_test.csv
exit
