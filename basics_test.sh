#!/bin/bash

# test whether files conform to PEP 8
pycodestyle style.py
pycodestyle get_column_stats.py

# test random inputs and random column selection
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data1.txt
python get_column_stats.py --file_name data1.txt --col_number $(( $RANDOM % 5))

# test known inputs for expected values
V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data2.txt
python get_column_stats.py --file_name data2.txt --col_number $(( $RANDOM % 5))

# test error handling for non-integer input in text file
V=a
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data3.txt
python get_column_stats.py --file_name data3.txt --col_number $(( $RANDOM % 5))

# test error handling for incorrect column indexing
V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data4.txt
python get_column_stats.py --file_name data4.txt --col_number 6

# test error handling for non-existant file
python get_column_stats.py --file_name data5.txt --col_number 3

# print exit code, should be 1
echo $?

