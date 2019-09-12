#!/bin/bash

pycodestyle style.py
pycodestyle get_column_stats.py


(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data1.txt

python get_column_stats.py --file_name data1.txt --col_number $(( $RANDOM % 5))

V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data2.txt

python get_column_stats.py --file_name data2.txt --col_number $(( $RANDOM % 5))

V=a
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data3.txt

python get_column_stats.py --file_name data3.txt --col_number $(( $RANDOM % 5))


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data4.txt

python get_column_stats.py --file_name data4.txt --col_number 6


echo $?

