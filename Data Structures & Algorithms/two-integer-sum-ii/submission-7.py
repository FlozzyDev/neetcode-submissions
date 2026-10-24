class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # count 3
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            res = numbers[l] + numbers[r]
            if res == target:
                return [l + 1, r + 1]
            elif res < target:
                l += 1
            else:
                r -= 1
        return []