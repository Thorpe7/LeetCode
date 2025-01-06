from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l1_pointer = m - 1
        l2_pointer = n - 1
        merge_pointer = m + n - 1

        while l1_pointer >= 0 and l2_pointer >= 0:
            if nums2[l2_pointer] > nums1[l1_pointer]:
                nums1[merge_pointer] = nums2[l2_pointer]
                merge_pointer -= 1
                l2_pointer -= 1
            else:
                nums1[merge_pointer] = nums1[l1_pointer]
                merge_pointer -= 1
                l1_pointer -= 1

        while l2_pointer >= 0:
            nums1[merge_pointer] = nums2[l2_pointer]
            merge_pointer -= 1
            l2_pointer -= 1
