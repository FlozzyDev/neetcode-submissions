class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arraySet = set(nums)

        if len(arraySet) == len(nums):
            return False
        else:
            return True