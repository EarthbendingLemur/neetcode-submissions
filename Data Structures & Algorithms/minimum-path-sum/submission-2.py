class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float('inf')] * COLS for _ in range(ROWS)]
        dp[0][0] = grid[0][0]
        paths = [(-1, 0), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                # Iterate through paths for r, c
                for dr, dc in paths:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or col < 0 or col == COLS):
                        continue
                    dp[r][c] = min(grid[r][c] + dp[row][col], dp[r][c])

        return dp[-1][-1]
