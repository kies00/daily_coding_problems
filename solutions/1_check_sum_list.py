"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import unittest


def check_sum(a_list, k):
    my_hash = {}
    
    for element in a_list:
        if element in my_hash:
            return True
        needs = k - element
        my_hash[needs] = element

    return False


class MyTestSuite(unittest.TestCase):

    def test_given_example(self):
        self.assertEqual(check_sum([10, 15, 3, 7], 17), True)

    def test_no_elements_in_list(self):
        self.assertEqual(check_sum([], 2), False)

    def test_sum_is_zero(self):
        self.assertEqual(check_sum([], 0), False)

    def test_list_not_empty_sum_is_zero(self):
        self.assertEqual(check_sum([1, 3], 0), False)

    def test_multiple_solutions(self):
        self.assertEqual(check_sum([4, 3, 5, 9, 1, 17, 10, 12, 6], 13), True)

    def test_no_solution(self):
        self.assertEqual(check_sum([4, 3, 5, 9, 1, 17, 10, 12, 6], 50), False)

if __name__ == '__main__':
    unittest.main()
