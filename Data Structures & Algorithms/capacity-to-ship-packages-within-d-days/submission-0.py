class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max_cap = 0
        for w in weights:
            min_cap = max(w, min_cap)
            max_cap += w
        
        res = max_cap
        def loadingSim(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True

        while min_cap <= max_cap:
            cap = (min_cap + max_cap) // 2
            if loadingSim(cap):
                res = min(res, cap)
                max_cap = cap - 1
            else:
                min_cap = cap + 1
        
        return res 
                