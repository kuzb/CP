import unittest
from math import sqrt
from main import binarySearch, findFVEG, findMSSL, findMIDL, findSQRT


class binarySearchVariations(unittest.TestCase):
    def test_binary_search_found(self):
        ls = [12, 19, 49, 59, 72, 88, 108, 121, 146, 152, 168, 201, 212, 218, 223]
        target = 72
        index = 4
        self.assertEqual(binarySearch(ls, target), index)

    def test_binary_search_not_found(self):
        ls = [12, 19, 49, 59, 72, 88, 108, 121, 146, 152, 168, 201, 212, 218, 223]
        target = 99
        index = -1
        self.assertEqual(binarySearch(ls, target), index)

    def test_get_first_value_greater(self):
        ls = [12, 19, 49, 59, 72, 88, 108, 121, 146, 152, 168, 201, 212, 218, 223]
        target = 21
        index = 2
        self.assertEqual(findFVEG(ls, target), index)

    def test_get_first_value_equal(self):
        ls = [12, 19, 49, 59, 72, 88, 108, 121, 146, 152, 168, 201, 212, 218, 223]
        target = 201
        index = 11
        self.assertEqual(findFVEG(ls, target), index)

    def test_get_minimum_in_shifted_sorted_list(self):
        ls = [5, 6, 7, 8, 1, 2, 3, 4]
        minimum = 1
        self.assertEqual(findMSSL(ls), minimum)

    def test_get_minimum_in_shifted_sorted_list_2(self):
        ls = [49, 59, 72, 88, 108, 121, 146, 152, 168, 201, 212, 218, 223, 12, 19]
        minimum = 12
        self.assertEqual(findMSSL(ls), minimum)

    def test_get_maximum_in_increasing_decreasing_list(self):
        ls = [12, 49, 58, 65, 72, 108, 146, 168, 212, 223, 218, 201, 152, 121, 88, 59, 19]
        maximum = 223
        self.assertEqual(findMIDL(ls), maximum)

    def test_get_maximum_in_increasing_decreasing_list2(self):
        ls = [72, 108, 212, 223, 218, 201, 152, 121, 88, 59, 19]
        maximum = 223
        self.assertEqual(findMIDL(ls), maximum)

    def test_get_maximum_in_increasing_decreasing_list3(self):
        ls = [12, 49, 72, 108, 146, 168, 212, 223, 218, 201, 152, 19]
        maximum = 223
        self.assertEqual(findMIDL(ls), maximum)

    def test_get_maximum_in_increasing_decreasing_list4(self):
        ls = [2, 3, 4, 6, 9, 12, 11, 8, 6, 4, 1]
        maximum = 12
        self.assertEqual(findMIDL(ls), maximum)

    def test_find_sqrt(self):
        element = 14
        precision = 5
        answer = str(findSQRT(element, pow(10, -precision)))[:precision]
        result = str(sqrt(element))[:precision]
        self.assertEqual(answer, result)


if __name__ == "__main__":
    unittest.main()
