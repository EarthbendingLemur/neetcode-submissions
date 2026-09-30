class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1, math.ceil(x / 2)

        while l <= h:
            m = (l + h) // 2
            sq = m * m
            if sq == x:
                return m
            elif sq < x:
                l = m + 1
            else:
                h = m - 1
        
        return h