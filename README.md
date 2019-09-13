# best-practices
## Project Description:
In this project, we ensure that two files **get_column_stats.py** and **style.py** adhere to best practices for code development. 
- **get_column_stats.py** takes two inputs from the user: a text file and a column number. This script then finds the mean and standard deviation of the text file values for the specified column number.  The file basics_test.sh tests both of these files to ensure they handle exceptions and follow PEP 8 style.
- **style.py** has limited functionality, but is used to ensure we adhere to PEP 8 style. 

In addition, running file **basics_test.sh** is a test to ensure that **get_column_stats.py** and **style.py** follow best practices and are behaving as expected. This test file does not provide additional functionality to the user.

## How to use this project
**get_column_stats.py** requires two user inputs: a text file of numeric values, and column number.
For instance, suppose you have a text file called **text_values.txt** that is composed of the following numeric values:

1 5 7  
2 0 8  
9 8 3
 
Suppose also that you would like to perform get_column_stats on the second column. Then you should execute the following command in your terminal. (Note that python's indexing begins at 0, so to select the second (middle) column in the text file, provide the column number input of 1.)
 
 ```
 python get_column_stats.py --file_name text_values.txt --col_number 1 
 ```

## How to install software
To use this project, you will need to create a conda environment with python 3 installed as well as the library called 'pycodestyle'. Follow the directions below in terminal to set up your environment.

```
$ conda create --yes -n swe4s
$ conda install --yes python=3.6
$ conda activate swe4s
$ conda install -y pycodestyle
```
Note: retrieve the project files with the following command:
```
git clone <URL-for-this-repo>
```

