from typing import List


class ElementRemover:
    def remove_element(self, nums: List[int], val: int) -> int:
        # Given a list, remove all instances of `val`
        # Do this in-place
        # Return the number of elements (k) in nums
        # That are not equal to val

        # Change nums so first k elements do not contain val
        # the remaining elements of nums are not important

        # --- Similar to remove dups ---
        # Can use pointer to check for value, if not value place at index

        if len(nums) == 0:
            return 0

        insert_at_index = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[insert_at_index] = nums[idx]
                insert_at_index += 1

        return insert_at_index
