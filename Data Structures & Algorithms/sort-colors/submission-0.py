class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # step 1: set count and iterate each
        count = [0] * 3
        for n in nums:
            count[n] += 1 
        # step 2: set an index, and modify the original list per count
        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

        