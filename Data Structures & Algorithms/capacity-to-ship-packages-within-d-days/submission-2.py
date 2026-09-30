class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Determine min and max capacities
        min_cap = max_cap = 0
        for w in weights:
            max_cap += w
            min_cap = max(w, min_cap)


        def canShip(cap):
            ships, capNow = 1, 0

            for w in weights:
                if capNow + w > cap:
                    ships += 1
                    capNow = 0
                capNow += w
            
            return ships <= days

        res = max_cap
        while min_cap < max_cap:
            cap = min_cap + (max_cap - min_cap) // 2
            if canShip(cap): 
                res = min(res, cap)
                max_cap = cap
            else:
                min_cap = cap + 1

        return res