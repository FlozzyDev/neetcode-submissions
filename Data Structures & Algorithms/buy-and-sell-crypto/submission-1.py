class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = prices[0]

        for sell in prices:
            best = max(best, sell - low)
            low = min(low, sell)
        return best
            