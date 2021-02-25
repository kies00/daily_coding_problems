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

        result = [0] * len(nums)

        result[-1] = 1
        for idx in range(len(nums) - 2, -1, -1):
            result[idx] = result[idx + 1] * nums[idx + 1]

        leftside_prod = 1
        for idx in range(len(nums)):
            result[idx] = leftside_prod * result[idx]
            leftside_prod *= nums[idx]

        return result


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

