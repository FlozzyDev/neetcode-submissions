class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # count 2
        longest = 0
        mySet = set(nums)
        for n in mySet:
            if (n - 1) not in mySet:
                length = 1
                while n + length in mySet:
                    length += 1
                longest = max(longest, length)
        return longest




        