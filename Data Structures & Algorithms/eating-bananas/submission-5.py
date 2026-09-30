class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        
        low_k, high_k = 1, max(piles)
        min_k = high_k
        while low_k < high_k:
            mid_k = (low_k + high_k) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid_k)
            if hours <= h:
                min_k = min(mid_k, min_k)
                high_k = mid_k
            else:
                low_k = mid_k + 1
            
        
        return min_k
