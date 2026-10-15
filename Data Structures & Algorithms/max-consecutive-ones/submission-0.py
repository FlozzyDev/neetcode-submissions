class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currentCount = 0
        for i in nums:
            if i == 1:
                currentCount += 1
                if maxCount < currentCount:
                    maxCount = currentCount
            elif i != 1:
                currentCount = 0
        return maxCount
