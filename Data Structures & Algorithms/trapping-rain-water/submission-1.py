class Solution:
    def trap(self, height: List[int]) -> int:
        "This will be the memory optimized solution using 2 pointer instead of holding 2 arrays"
        #  set starting variables
        l, r  = 0, len(height) -1
        left_max, right_max = height[l], height[r]
        res = 0

        # two pointer loop
        while l < r:
            # check which wall is lower - iterate that pointer and set new max + calculate water based on height
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res

        


        