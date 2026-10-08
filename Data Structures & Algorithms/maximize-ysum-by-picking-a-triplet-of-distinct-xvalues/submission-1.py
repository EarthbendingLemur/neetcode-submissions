class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        best_x = {}

        for i in range(len(x)):
            if x[i] not in best_x or best_x[x[i]] < y[i]:
                best_x[x[i]] = y[i]
            
        
        if len(best_x) < 3:
            return -1

        res = 0
        for _ in range(3):
            x_i, y_i = max(best_x.items(), key = lambda x:x[1])
            res += y_i
            del best_x[x_i]
        return res