class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l, h = max(weights), sum(weights)

        def canShip(cap):
            res = 1
            curCap = 0
            for w in weights:
                if curCap + w > cap:
                    res += 1
                    curCap = 0
                curCap += w
            return res <= days
        
        res = h
        while l <= h:
            m = (h + l) // 2
            if canShip(m):
                res = m
                h = m - 1
            else:
                l = m + 1
            
        
        return res
        