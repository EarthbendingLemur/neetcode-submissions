class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L, R = 0, 1

        if len(prices) < 2:
            return res
        
        while R < len(prices):
            pft = prices[R] - prices[L]

            if prices[L] < prices[R]:
                res = max(pft, res)
            else:
                L = R
            R += 1

        
        return res
        
