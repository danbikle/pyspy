#!/bin/bash

# ~/pyspy/bin/noon50.bash
# This should be run from cron with an entry like this:
# 50 12 * * mon,tue,wed,thu,fri ${HOME}/pyspy/bin/noon50.bash > /tmp/noon50_bash.txt 2>&1
. ${HOME}/pyspy/pyspy_env.bash
# I should get prices and most recent price:
${PYSPY}/bin/wgetGSPC.bash

# I should generate features from prices:
cd $DDATA
python ${PYSPY}/py/genf.py GSPC2.csv
