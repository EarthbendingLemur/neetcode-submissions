class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        if len(set(x)) < 3:
            return -1
        
        hp = []

        for i in range(len(x)):
            heapq.heappush(hp, (-y[i], x[i]))
        
        res = []
        res_val = 0
        while len(res) < 3:
            val, x_i = heapq.heappop(hp)
            if not res or x_i not in res:
                res.append(x_i)
                res_val += -val

        return res_val