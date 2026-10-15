class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        if len(nums) == len(mySet):
            return False
        else:
            return True
