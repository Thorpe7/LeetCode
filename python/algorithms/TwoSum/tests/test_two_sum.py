""" Unit test for two_sum.py """

from unittest import TestCase

from src.two_sum import TwoSum


class TestTwoSum(TestCase):
    def setUp(self):
        self.expected1 = [0, 1]
        self.expected2 = [1, 2]
        self.expected3 = [0, 1]

    def test_run_two_sum(
        self,
    ) -> None:
        twoSumObj = TwoSum()

        # Test Case 1
        nums1 = [2, 7, 11, 15]
        target1 = 9
        output1 = twoSumObj.run_two_sum(nums=nums1, target=target1)
        output1.sort()
        self.assertEqual(self.expected1, output1)

        # Test Case 2
        nums2 = [3, 2, 4]
        target2 = 6
        output2 = twoSumObj.run_two_sum(nums=nums2, target=target2)
        output2.sort()
        self.assertEqual(self.expected2, output2)

        # Test Case 3
        nums3 = [3, 3]
        target3 = 6
        output3 = twoSumObj.run_two_sum(nums=nums3, target=target3)
        output3.sort()
        self.assertEqual(self.expected3, output3)
