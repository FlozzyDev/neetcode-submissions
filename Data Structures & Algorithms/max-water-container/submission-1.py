class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(h) * w(p2=p1)
        p1,p2 = 0, len(heights) - 1
        maxH = 0

        while p1 < p2:
            h = min(heights[p1], heights[p2])
            w = (p2) - (p1)
            maxH = max(h*w, maxH)

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxH

        