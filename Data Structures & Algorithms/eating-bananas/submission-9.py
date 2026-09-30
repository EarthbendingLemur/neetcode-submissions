class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)
        res = max_k
        while min_k < max_k:
            k = (min_k + max_k) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(k, res)
                max_k = k
            else:
                min_k = k + 1
    
        return res