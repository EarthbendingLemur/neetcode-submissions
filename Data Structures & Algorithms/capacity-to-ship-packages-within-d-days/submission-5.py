class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Determine min and max capacities
        min_cap = max(weights)
        max_cap = sum(weights)

        def canShip(cap) -> bool:
            ships, curCap = 1, 0
            for w in weights:
                if curCap + w > cap:
                    ships += 1
                    curCap = 0
                curCap += w

            return ships <= days


        res = max_cap
        while min_cap < max_cap:
            cap = (min_cap + max_cap) // 2
            if canShip(cap):
                res = min(cap, res)
                max_cap = cap
            else:
                min_cap = cap + 1
            
        
        return res
