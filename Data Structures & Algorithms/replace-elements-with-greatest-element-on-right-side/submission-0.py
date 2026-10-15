class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans = [0] * length
        rightMax = -1
        for i in range (length - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans