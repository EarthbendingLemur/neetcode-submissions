class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1

        if len(prices) < 2:
            return 0

        
        res = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                res = max(profit, res)
            else:
                buy = sell
            sell += 1
        return res
