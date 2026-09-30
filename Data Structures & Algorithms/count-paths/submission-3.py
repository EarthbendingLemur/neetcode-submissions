class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = 1
        for i in range(1,m):
            dp[i][0] = 1
        
        for i in range(1, n):
            dp[0][i] = 1
        
        for r in range(1,m):
            for c in range(1,n):                
                up_neigh = dp[r - 1][c]
                left_neigh = dp[r][c - 1]
                dp[r][c] = up_neigh +  left_neigh
        



        print(dp)
        return dp[-1][-1]