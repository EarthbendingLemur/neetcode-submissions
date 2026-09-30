class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, mx = 0, 1
        r = mx
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[mn]
            max_profit = max(max_profit, profit)
            if mn < r and prices[r] < prices[mn]:
                mn = r
            if prices[r] > prices[mx]:
                mx = r
            r += 1

        return max_profit