import unittest

from main import checkSubsetSum


class Subsets(unittest.TestCase):
    def test_check_subset_sum(self):
        subset = [23, 21, 12, 16, 47, 24, 74]
        the_sum = 40
        expected = [16, 24]
        self.assertEqual(checkSubsetSum(subset, the_sum), expected)


if __name__ == "__main__":
    unittest.main()
