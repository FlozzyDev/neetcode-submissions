class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memBank = {}

        for i in range(len(nums)):
            compare = target - nums[i]
            if compare in memBank:
                return [memBank[compare], i]
            else:
                memBank[nums[i]] = i
        return [-1,-1]
        
                