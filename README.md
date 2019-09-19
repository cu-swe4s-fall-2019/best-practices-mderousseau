# best-practices
## Project Description:
In this project, we ensure that two files **get_column_stats.py** and **style.py** adhere to best practices for code development. 
- **get_column_stats.py** takes three inputs from the user: a text file, a column number, and an operation ("mean" or "stdev"). This script then finds the mean or standard deviation of the text file values for the specified column number.  The file basics_test.sh includes functional tests to determine whether these files handle exceptions and follow PEP 8 style. In addition, the file basics_test.py includes unit tests to ensure that individual methods of get_column_stats.py perform as expected
- **style.py** has limited functionality, but is used to ensure we adhere to PEP 8 style. 

## How to use this project
**get_column_stats.py** requires three user inputs: a text file of numeric values, column number, and operation ("mean" for mean and "stdev" for standard deviation)
For instance, suppose you have a text file called **text_values.txt** that is composed of the following numeric values:

1 5 7  
2 0 8  
9 8 3
 
Suppose also that you would like to get the mean of the second column. Then you should execute the following command in your terminal. (Note that python's indexing begins at 0, so to select the second (middle) column in the text file, provide the column number input of 1.)
 
 ```
 python get_column_stats.py --file_name text_values.txt --col_number 1 --operation mean
 ```

## How to install software
To use this project, you will need to create a conda environment with python 3 installed as well as the libraries 'pycodestyle' and 'numpy'. A .travis.yml file is included in this repo which will install dependencies and set up the required environment. Alternatively, follow the directions below in terminal to set up your environment that will allow you to run the basic functionality in get_column_stats.py.

```
$ conda create --yes -n swe4s
$ conda install --yes python=3.6
$ conda activate swe4s
$ conda install -y pycodestyle
$ conda install -y numpy
```


