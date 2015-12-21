#!/bin/bash

# talib_demo.bash

# Demo:
# ~/pyspy/bin/talib_demo.bash

. ${HOME}/pyspy/pyspy_env.bash
cd ${PYSPY}/demodata/

python ${PYSPY}/py/talib_demo.py ftrGSPC2.csv

exit
