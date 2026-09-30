class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)

        print(min_cap)
        print(max_cap)

        res = max_cap

        def canShip(cap):
            ships = 1
            cur_cap = 0
            for w in weights:
                if cur_cap + w > cap:
                    ships += 1
                    cur_cap = 0
                cur_cap += w

            return ships <= days


        while min_cap < max_cap:
            cap = (min_cap + max_cap) // 2
            if canShip(cap):
                res = min(cap, res)
                max_cap = cap
            else:
                min_cap = cap + 1


        print(canShip(7))
        return res

