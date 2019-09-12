"""This script finds the mean and std. dev. for the column of a text file."""
import math
import argparse
import sys


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
            print('Is your column number an integer?')
            sys.exit(1)

        # handle exceptions that could be caused by using the provided
        # column number
        try:
            V.append(A[args.col_number])
        except TypeError:
            print('The column number should be an integer')
            sys.exit(1)
        except IndexError:
            print('The column number should be an existing column in the file')
            sys.exit(1)

    # calculate mean and standard deviation
    mean = sum(V)/len(V)
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
