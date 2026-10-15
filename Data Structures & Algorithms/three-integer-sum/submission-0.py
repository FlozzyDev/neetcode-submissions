class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # if value over 0, break since it can never == 0
            if a > 0:
                break
            # if we find a duplicate, continue
            if i > 0 and a == nums[i - 1]:
                continue
            # set l ahead of i, and r to the end
            l, r = i + 1, len(nums) - 1
            while l < r:
                # set threeSum value
                threeSum = a + nums[l] + nums[r]
                # check if above or below 0
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                # else append, move both, and check left for duplicates
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
 

        