""" Two Sum Solution. """

from typing import List


class TwoSum:
    def run_two_sum(self, nums: List[int], target: int) -> List[int]:
        previous_nums = {}

        for idx, ele in enumerate(nums):

            # Find compliment number
            compliment_num = target - ele

            # If the compliment is already in the values, return indices
            if (
                compliment_num in previous_nums.keys()
                and idx not in previous_nums.values()
            ):
                return [previous_nums[compliment_num], idx]
            else:
                previous_nums[ele] = idx

        else:
            print(f"No two numbers found to add to {target}")


"""
Explanation:

- Iterating through a list costs O(n) time complexity.

- Using a brute force method would cost O(n^2) time complexity.

- Using a dictionary (HashMap) to store the previous numbers we come across, can reduce the time complexity.

--- Why does it reduce the time complexity? ---
    --> Because to look up a value in a dictionary take O(1) time complexity
    --> So looking up the compliment number in the dictionary for each element in the list costs 0(n*1) = O(n) time complexity since we drop constants.
"""
