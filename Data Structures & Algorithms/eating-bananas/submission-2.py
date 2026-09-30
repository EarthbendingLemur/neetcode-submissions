class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_k = 1
        max_k = max(piles)
        sol = max_k
        while min_k <= max_k:
            speed = (min_k + max_k) // 2

            time_to_eat = 0
            for p in piles:
                time_to_eat += math.ceil(float(p) / speed)
            if  time_to_eat <= h:
                sol = speed
                max_k = speed - 1
            else:
                min_k = speed + 1

        return sol