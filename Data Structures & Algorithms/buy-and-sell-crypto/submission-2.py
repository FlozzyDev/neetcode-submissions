class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #count 4
        best = 0
        low = prices[0]

        for p in prices:
            best = max(best, p - low)
            low = min(low, p)
        return best
            