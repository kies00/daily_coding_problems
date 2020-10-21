"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Note: This is the no division solution
"""
import unittest


class Solution:   
    def array_prod(self, nums):
        if len(nums) == 0:
            return []

        prod = 1
        prod_map = {}
        for idx in reversed(range(len(nums))):
            prod_map[idx] = prod
            prod *= nums[idx]

        prod = 1
        final_result = []
        for idx, number in enumerate(nums):
            final_result.append(prod * prod_map[idx])
            prod *= number

        return final_result


class MyTestSuite(unittest.TestCase):
    def test_given_example(self):
        self.assertEqual(sol.array_prod([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_empty_list(self):
        self.assertEqual(sol.array_prod([]), [])

    def test_1(self):
        self.assertEqual(sol.array_prod([3]), [1])

    def test_2(self):
        self.assertEqual(sol.array_prod([1, 3, 4]), [12, 4, 3])

    def test_3(self):
        self.assertEqual(sol.array_prod([0, 3, 5]), [15, 0, 0])

    def test_4(self):
        self.assertEqual(sol.array_prod([6, 8, 9]), [72, 54, 48])

    def test_5(self):
        self.assertEqual(sol.array_prod([1, 1, 1]), [1, 1, 1])

    def test_6(self):
        self.assertEqual(sol.array_prod([1, 4, 6, 12, 19, 30]), [164160, 41040, 27360, 13680, 8640, 5472])


if __name__ == '__main__':
    sol = Solution()
    unittest.main()

