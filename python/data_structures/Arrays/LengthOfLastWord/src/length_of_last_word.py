class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        cleaned_words = [x for x in words if x != ""]
        last = cleaned_words[-1]
        return len(last)
