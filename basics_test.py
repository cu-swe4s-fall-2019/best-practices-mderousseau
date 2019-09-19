import unittest
from get_column_stats import mean_col
from get_column_stats import stdev_col
import numpy as np
import random


# Unit testing mean_col and stdev_col methods
# for planned values
class TestColumnStats(unittest.TestCase):
    def test_mean(self):
        col = np.array([1, 1, 1])
        self.assertEqual(mean_col(col), 1)

    def test_stdev(self):
        col = np.array([1, 1, 1])
        self.assertEqual(stdev_col(col), 0)

# Unit tests for random columns, random length
# do it many times
    def test_mean_rand(self):
        for i in range(100):
            # column of random numbers of random length
            col_len = random.randint(2, 10)
            col = random.sample(range(100), col_len)
            self.assertEqual(mean_col(col), np.mean(col))

    def test_stdev_rand(self):
        for i in range(100):
            col_len = random.randint(2, 10)
            col = random.sample(range(100), col_len)
            stdev1 = round(stdev_col(col), 5)
            stdev2 = round(np.std(col), 5)
            self.assertEqual(stdev1, stdev2)

# Tests for error handling
# test for non-numbers in array
    def test_mean_non_numbers(self):
        col = ["a", "b", "c"]
        self.assertIsNone(mean_col(col))

    def test_stdev_non_numbers(self):
        col = ["a", "b", "c"]
        self.assertIsNone(stdev_col(col))

    # tests for non-column input to method
    def test_stdev_non_column(self):
        col = [[1, 2, 3], [4, 5, 6]]
        self.assertIsNone(stdev_col(col))

    def test_mean_non_column(self):
        col = [[1, 2, 3], [4, 5, 6]]
        self.assertIsNone(mean_col(col))
