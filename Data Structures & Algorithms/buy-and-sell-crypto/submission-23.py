class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxP = 0
        while R < len(prices):  
            if prices[R] < prices[L]:
                L = R
            profit = prices[R] - prices[L]
            maxP = max(maxP, profit)
            R += 1
        
        return maxP