class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left_pointer = 0
        right_pointer = len(arr)
        middle = 0

        while left_pointer < right_pointer:
            middle = left_pointer + (right_pointer - left_pointer) // 2
            missing_nums = (
                arr[middle] - middle - 1
            )  # Numbers missing before the current element
            # To calculate what the kth missing positive integer is
            # We know there are 5 missing elements, and that we have traversed x number of indices
            # So if we had traveled a complete array, we would have traveled over the current number
            # of elements plus the missing elements as well
            # so kth missing element = k + number elements we traversed over

            if k == missing_nums:
                print("middle idx was used...")
                return k + middle
            elif missing_nums < k:
                left_pointer = middle + 1
            else:
                right_pointer = middle

        return k + left_pointer
