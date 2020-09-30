import unittest

from subset_sum import check_sum


class HighScoresTest(unittest.TestCase):
    def test_check_sum(self):
        subset = [23, 21, 12, 16, 47, 24, 74]
        the_sum = 40
        expected = [16, 24]
        self.assertEqual(check_sum(subset, the_sum), expected)


if __name__ == "__main__":
    unittest.main()
