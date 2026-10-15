class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memBank = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in memBank:
                return [memBank[diff], i]
            else:
                memBank[nums[i]] = i
        return []