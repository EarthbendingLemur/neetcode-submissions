class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_piles, max_piles  = 1, sum(piles)
        res = max_piles
        while min_piles <= max_piles:
            k = (min_piles + max_piles) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                max_piles = k - 1
            else:
                min_piles =  k + 1
        

        return res