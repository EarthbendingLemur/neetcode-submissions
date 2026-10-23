class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_left = values[0]
        res = 0
        for i in range(1, len(values)):
            res = max(res, best_left + values[i] - i)
            best_left = max(best_left, values[i] + i)
        return res
