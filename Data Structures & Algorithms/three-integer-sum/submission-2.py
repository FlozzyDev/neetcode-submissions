class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set variables / sort
        res = []
        n = len(nums)
        nums.sort()
        # Start O_loop
        for i in range(len(nums)):
            # i condictionals (2)
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # set lo (i+1)/hi(n-1)
            lo, hi = i + 1, n-1
            #loop lo/hi
            while lo < hi:
                # summ
                summ = nums[i] + nums[lo] + nums[hi]
                # if we get the right summ
                if summ == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                # if summ < 0 or else?
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
        # return
        return res
        
 

        