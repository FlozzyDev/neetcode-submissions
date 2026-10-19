class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count 2
        mySet = set(nums)
        if len(mySet) != len(nums):
            return True
        return False
