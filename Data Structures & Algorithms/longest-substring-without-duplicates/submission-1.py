class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        best = 0
        left = 0

        for i, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = i
            best = max(best, i - left + 1)
        return best


