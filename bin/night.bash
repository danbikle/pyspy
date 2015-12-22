#!/bin/bash

# ~/pyspy/bin/night.bash
# Demo:
# ~/pyspy/bin/night.bash
. ${HOME}/pyspy/pyspy_env.bash
# I should get prices and most recent price:
${PYSPY}/bin/wgetGSPCnight.bash

# I should generate features from prices:
cd $DDATA
python ${PYSPY}/py/genf.py          GSPC2.csv
python ${PYSPY}/py/genf_talib.py ftrGSPC2.csv
