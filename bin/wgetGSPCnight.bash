#!/bin/bash

# ~/pyspy/bin/wgetGSPCnight.bash

# This script should get prices at night.
. ${HOME}/pyspy/pyspy_env.bash

mkdir -p $DDATA
cd       $DDATA

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.csv

wget --output-document=${TKR}.csv http://ichart.finance.yahoo.com/table.csv?s=${TKRH}
echo 'cdate,cp'                                      > ${TKR}2.csv
grep -v Date ${TKR}.csv|awk -F, '{print $1 "," $5}' >> ${TKR}2.csv

exit
