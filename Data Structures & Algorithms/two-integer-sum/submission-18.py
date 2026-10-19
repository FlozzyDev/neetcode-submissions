class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # count 2
        mem = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mem:
                return [mem[diff], i]
            else:
                mem[nums[i]] = i
        return []