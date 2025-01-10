class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2):
            shorter_list = nums2
            longer_list = nums1
        else:
            shorter_list = nums1
            longer_list = nums2

        intersection_list = []
        for idx in range(len(shorter_list)):

            left_pointer = 0
            right_pointer = len(longer_list) - 1

            while (
                left_pointer <= right_pointer
            ):  # One of the cases where left and right pointer could be equal to each other, but we still need search logic to continue
                middle = left_pointer + (right_pointer - left_pointer) // 2
                print(longer_list[middle])

                if longer_list[middle] == shorter_list[idx]:
                    if shorter_list[idx] not in intersection_list:
                        intersection_list.append(shorter_list[idx])
                        break

                if shorter_list[idx] >= longer_list[middle]:
                    left_pointer = middle + 1

                if shorter_list[idx] < longer_list[middle]:
                    right_pointer = middle - 1

        return intersection_list
