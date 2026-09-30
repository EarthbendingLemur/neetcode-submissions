class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        for c in range(COLS):
            dp[0][c] = points[0][c]

        for r in range(1, ROWS):
            for c in range(COLS):
                possible_scores = dp[r - 1].copy()
                for i in range(len(possible_scores)):
                    possible_scores[i] -= abs(c - i)
                dp[r][c] = max(possible_scores) + points[r][c]


        return max(dp[-1])

        
        