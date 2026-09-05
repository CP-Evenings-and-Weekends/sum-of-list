import unittest

from sum_of_list import sum_of_list


class TestSumOfList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_of_list([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_of_list([5]), 5)

    def test_multiple_elements(self):
        self.assertEqual(sum_of_list([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_list([-1, 1, -1]), -1)


# Stretch: uncomment once you've written deep_sum (see the README).
#
# from sum_of_list import deep_sum
#
# class TestDeepSum(unittest.TestCase):
#     def test_nested_lists(self):
#         self.assertEqual(deep_sum([1, [2, [3, 4]], 5]), 15)


if __name__ == "__main__":
    unittest.main()
