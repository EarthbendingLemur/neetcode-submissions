class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <= r:
            m = (l + r) // 2
            lower_bound = (m * (m + 1)) // 2
            if lower_bound > n:
                r = m - 1
            else:
                l = m + 1
                res = max(res, m)
        
        return res
