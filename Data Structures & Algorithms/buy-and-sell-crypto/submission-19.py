class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        if len(prices) < 2:
            return 0
        maxP = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        

        return maxP

