class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        best_x = {}
        K = 3
        for i in range(len(x)):
            if x[i] not in best_x or best_x[x[i]] < y[i]:
                best_x[x[i]] = y[i]
            
        
        if len(best_x) < K:
            return -1

        res = 0
        for _ in range(K):
            x_i, y_i = max(best_x.items(), key = lambda x:x[1])
            res += y_i
            del best_x[x_i]

        return res