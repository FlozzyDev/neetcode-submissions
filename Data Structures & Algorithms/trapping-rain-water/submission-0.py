class Solution:
    def trap(self, height: List[int]) -> int:
        "This is the O(n) memory solution which is not ideal - holding 2 arrays of height"
        # if we have no list, we get no water
        if not height:
            return 0
        # set starting variables
        n = len(height)
        l_wall, r_wall = 0, 0
        max_left = [0] * n
        max_right = [0] * n
        summ = 0

        # loop to build height arrays
        for i in range(n):
            j = -i - 1 # iterate the right at the same time by setting it to negative i
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        # We have heights mapped, now iterate to find potential water - height
        for i in range(n):
            # potential is whatever wall is lower
            pot_water = min(max_left[i], max_right[i])
            # subtract the height
            summ += max(0, pot_water - height[i])
        return summ
        


        