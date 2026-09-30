class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = [[1] * COLS for _ in range(ROWS)]

        # init rows and cols dependent on obstacle detection

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # first row
        for c in range(1, COLS):
            if obstacleGrid[0][c] == 1:
                dp[0][c] = 0
            else:
                dp[0][c] = dp[0][c - 1]

        # first column
        for r in range(1, ROWS):
            if obstacleGrid[r][0] == 1:
                dp[r][0] = 0
            else:
                dp[r][0] = dp[r - 1][0]
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]


        print(dp)
        return dp[-1][-1] 