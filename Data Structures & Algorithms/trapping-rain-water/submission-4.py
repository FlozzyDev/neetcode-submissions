class Solution:
    def trap(self, height: List[int]) -> int:
        "This will be the memory optimized solution using 2 pointer instead of holding 2 arrays"
        # count 4
        l,r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        return res


        


        