class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # count 3
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            maxArea = max(maxArea, a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea



        

                




            


        