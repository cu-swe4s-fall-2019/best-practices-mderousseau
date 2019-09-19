#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test that mean from inputs returns what we expect
run basic_mean python get_column_stats.py --operation mean --col_number 0 --file_name column_file.txt
assert_in_stdout 1
assert_exit_code 0

# test that std dev from inputs returns what we expect
run basic_std_dev python get_column_stats.py --operation stdev --col_number 0 --file_name column_file.txt
assert_in_stdout 0
assert_exit_code 0

# test that file conforms to PEP 8
run basic_pep_8 pycodestyle get_column_stats.py
assert_exit_code 0

# test error handling for non-integer in text file
run non_integer_file python get_column_stats.py --operation mean --col_number 0 --file_name not_integers.txt
assert_exit_code 1
assert_in_stdout "Are the values in the files numbers?"

# test error handling for non-existant file
run basic_no_file python get_column_stats.py --operation stdev --col_number 0 --file_name no_file.txt
assert_exit_code 1
assert_in_stdout "Could not find the file"

# test error handling for wrong column number (stdev)
run basic_no_file python get_column_stats.py --operation stdev --col_number 1 --file_name column_file.txt
assert_exit_code 1
assert_in_stdout 'The column number should be an existing column'

# test whether errors occur with many random inputs
# and with diff num of columns for stdev
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM">data1.txt
    run basic_random_inputs python get_column_stats.py --operation stdev --col_number $(( $RANDOM % 5)) --file_name data1.txt
    assert_exit_code 0
    assert_stdout;
done )

# test whether errors occur with many random inputs
# and with diff num of columns for mean
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM">data1.txt
    run basic_random_inputs python get_column_stats.py --operation mean --col_number $(( $RANDOM % 5)) --file_name data1.txt
    assert_exit_code 0
    assert_stdout;
done )