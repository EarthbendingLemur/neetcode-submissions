class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp sol
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        res = 0
        for c in range(COLS):
            dp[0][c] = 1 if matrix[0][c] == "1" else 0
            res = max(res, dp[0][c])
        for r in range(ROWS):
            dp[r][0] = 1 if matrix[r][0] == "1" else 0
            res = max(res, dp[r][0])

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == "0":
                    continue

                top_left_diag = [0, 0, 0]
                top_left_diag[0] = dp[r - 1][c]
                top_left_diag[1] = dp[r][c - 1]
                top_left_diag[2] = dp[r - 1][c - 1]
                
                dp[r][c] = min(top_left_diag) + 1
                res = max(dp[r][c], res)
                
        print(dp)
        return res * res
