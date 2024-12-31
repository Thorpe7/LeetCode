""" Script for Leet Code question 26. Remove Duplicates from Sorted Array. """

from typing import List


class DupRemover:
    def remove_duplicates(nums: List[int]) -> int:
        """

        Pointer1 = i, is the index from the for loop
        Pointer2 = i-1, is the element behind the current value

        If they are the same, then i does not need to be put to the front of the list
        If they are different, it needs to be brought to the front of the list

        Define increment_index = 1; Set this to 1 as we will always know that the first element of a list will be unique as we haven't seen it yet.


        If Pointer1 != Pointer2, then we take the value of pointer2 and place it at location `increment_index`

        This won't work for empty list, so we have to check for empty lists and return [] if empty
        """

        if len(nums) == 0:
            return []

        idx_to_insert_at = 1  # Start the insert at 1 as 0 idx will be unique

        for idx in range(1, len(nums)):
            pointer1 = idx - 1
            pointer2 = idx

            if nums[pointer2] != nums[pointer1]:  # If we find a new val
                nums[idx_to_insert_at] = nums[pointer2]  # Insert at idx
                idx_to_insert_at += 1  # Increment position holder

        # Can just return this var, is len of unique elements
        return idx_to_insert_at
