from collections import defaultdict
class Solution:
    #count 2
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        best = 0
        left = 0 
        max_count = 0

        for right, c in enumerate(s):
            counts[c] += 1
            max_count = max(max_count, counts[c])
            while (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
