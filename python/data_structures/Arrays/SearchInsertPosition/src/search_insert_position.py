from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_pointer = 0
        end_pointer = len(nums) - 1
        pivot = 0

        while start_pointer <= end_pointer:
            pivot = start_pointer + (end_pointer - start_pointer) // 2

            if target == nums[pivot]:
                return pivot

            if target >= nums[pivot]:
                start_pointer = pivot + 1

            if target < nums[pivot]:
                end_pointer = pivot - 1

        return start_pointer
