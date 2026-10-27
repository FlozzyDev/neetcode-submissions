class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # count 3
        n = len(heights)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            # create var to hold our append index
            start = i
            # while number is too tall to continue
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i-index))
                start = index
            # append this height to the index it can reach back to
            stack.append((start, h))
        # check the area for all left in stack using length of height as the index to check against
        for index, height in stack:
            max_area = max(max_area, height * (n - index))
        return max_area
        