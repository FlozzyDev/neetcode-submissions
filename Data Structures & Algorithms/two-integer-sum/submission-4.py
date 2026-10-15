class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memBank = {}
        result = []

        for i in range(len(nums)):
            checkValue = target - nums[i]
            if checkValue in memBank:
                    result.append(memBank[checkValue])
                    result.append(i)
                    return result
            else:
                memBank[nums[i]] = i
        
                