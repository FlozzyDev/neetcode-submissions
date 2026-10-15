class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memBank = {}
        res = []

        for i in range(len(nums)):
            compare = target - nums[i]
            if compare in memBank:
                res.append(memBank[compare])
                res.append(i)
            else:
                memBank[nums[i]] = i
        return res
        
                