""" A thoroughly stupid question. """

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left_pointer = 0
        right_pointer = len(arr) - 1
        middle = 0

        while left_pointer <= right_pointer:
            middle = left_pointer + (right_pointer - left_pointer) // 2
            missing_nums = arr[middle] - middle - 1

            if missing_nums < k:
                left_pointer = middle + 1
            else:
                right_pointer = middle - 1

        return k + left_pointer
