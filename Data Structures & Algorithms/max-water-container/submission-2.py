class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            #calculate area
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            max_area = max(max_area, a)

            # move bars, keep higher
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
            


        