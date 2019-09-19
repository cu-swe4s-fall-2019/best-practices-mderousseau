"""This script finds the mean and std. dev. for the column of a text file."""
import math
import argparse
import sys


# define function to take mean of a column
def mean_col(V):
    try:
        mean = sum(V)/len(V)
    except TypeError:
        return None
        sys.exit(1)
    return(mean)


# define function to take standard deviation of a column
def stdev_col(V):
    try:
        stdev = math.sqrt(sum([(mean_col(V)-x)**2 for x in V]) / len(V))
    except TypeError:
        return None
        sys.exit(1)
    return(stdev)


def main():
    # Use argparse to provide user-inputted text file and column number
    parser = argparse.ArgumentParser(
                description='Argument parser',
                prog='the_good_way')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file',
                        required=True)
    parser.add_argument('--col_number',
                        type=int,
                        help="The column number",
                        required=True)

    parser.add_argument('--operation',
                        type=str,
                        help='mean or stdev')

    args = parser.parse_args()

    # handle various exceptions that may be caused by trying to open the file
    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        print('Could not find the file')
        sys.exit(1)
    except PermissionError:
        print('Could not open the file')
        sys.exit(1)

    V = []

    # fills V, an empty array with values from selected column
    for l in f:

        try:
            A = [int(x) for x in l.split()]
        except ValueError:
            print('Are the values in the files numbers?')
            sys.exit(1)

        # handle exceptions that could be caused by using the provided
        # column number
        try:
            V.append(A[args.col_number])
        except TypeError:
            print('The column number should be an integer')
            sys.exit(1)
        except IndexError:
            print('The column number should be an existing column')
            sys.exit(1)

    # calculate mean and standard deviation
    mean = mean_col(V)
    stdev = stdev_col(V)

    if args.operation == 'mean':
        print("mean:", mean)
    elif args.operation == 'stdev':
        print("stdev:", stdev)


if __name__ == '__main__':
    main()
