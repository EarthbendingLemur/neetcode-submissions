class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        low_k, max_k = 1, max(piles)
        min_k = max_k
        while low_k < max_k:
            k = (low_k + max_k) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / k)
            
            if time <= h:
                min_k = min(k, min_k)
                max_k = k
            else:
                low_k = k + 1
        

        return min_k


