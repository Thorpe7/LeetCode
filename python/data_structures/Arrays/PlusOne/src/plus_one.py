from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 0
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] != 9:
                print("here")
                digits[idx] = digits[idx] + 1
                carry_over = 0
                break
            else:
                digits[idx] = 0
                carry_over += 1
                if idx == 0:
                    digits.insert(0, 1)
                    break

        return digits
