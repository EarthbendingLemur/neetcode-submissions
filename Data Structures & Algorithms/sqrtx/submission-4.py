class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        res = 0
        while low <= high:
            m = low + (high - low) // 2
            if m * m > x:
                high = m - 1
            elif m * m < x:
                low = m + 1
                res = m
            else:
                return m
        
        return res
        