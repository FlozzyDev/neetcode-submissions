class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # count 2
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = 1 + mid
            else:
                r = mid - 1
        return -1