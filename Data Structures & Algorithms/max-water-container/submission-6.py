class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # count 2
        lp, rp = 0, len(heights) - 1
        max_area = 0
        while lp < rp:
            w = rp - lp
            h = min(heights[lp], heights[rp])
            a = w * h

            max_area = max(max_area, a)
            
            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        return max_area



        

                




            


        