#!/bin/bash

# ~/pyspy/bin/wgetGSPC.bash

# This script should get prices at 12:50 Calif time.

mkdir ~/ddata
cd    ~/ddata

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.csv ${TKR}.html

wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKRH}
cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKRH
# I should extract recent prices from html
python ~pyspy/py/extprice.py
# I should cat prices together
echo 'cdate,cp'                            > GSPC3.csv
cat GSPCrecent.csv GSPC2.csv|grep -v Date >> GSPC3.csv
cat GSPC3.csv                              > GSPC2.csv 

exit
