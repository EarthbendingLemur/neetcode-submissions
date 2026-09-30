class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        for c in range(COLS):
            dp[0][c] = points[0][c]

        for r in range(1, ROWS):
            left = [0] * COLS
            right = [0] * COLS
            left[0] = dp[r - 1][0]
            right[-1] = dp[r - 1][-1]

            for i in range(1, COLS):
                left[i] = max(left[i - 1] - 1, dp[r - 1][i])
            for i in range(COLS - 2, -1, -1):
                right[i] = max(right[i + 1] - 1, dp[r - 1][i])
            for c in range(COLS):
                dp[r][c] = max(left[c], right[c]) + points[r][c]



        return max(dp[-1])

        
        