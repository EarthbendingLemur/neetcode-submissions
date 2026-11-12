class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 0, ranks[0] * cars * cars

        res = -1
        def repair(t):
            count = 0
            for r in ranks:
                count += int(math.sqrt(t // r))
            return count

        while l <= r:
            m = (l + r) // 2

            repaired = repair(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

  