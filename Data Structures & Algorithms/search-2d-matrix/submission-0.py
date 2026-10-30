class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [num for sublist in matrix for num in sublist]
        l, r = 0 , len(nums) - 1
        print(r)

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

