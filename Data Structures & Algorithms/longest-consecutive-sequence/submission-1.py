class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        mySet = set(nums)
        sortedList = sorted(mySet)

        p1 = 0
        p2 = 1
        curr = 1
        max = 1

        while p2 < len(sortedList):
            if sortedList[p2] != sortedList[p1] + 1:
                if max < curr:
                    max = curr
                curr = 1
            else:
                curr += 1
                if max < curr:
                    max = curr
            p1 += 1
            p2 += 1
        return max
        