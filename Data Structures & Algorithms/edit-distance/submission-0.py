class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        ROWS, COLS = len(dp), len(dp[0])
        for c in range(1, COLS):
            dp[0][c] = dp[0][c - 1] + 1
        
        for r in range(1, ROWS):
            dp[r][0] = dp[r - 1][0] + 1
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    top_left_diag = [dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]]
                    dp[r][c] = min(top_left_diag) + 1

        
        for row in dp:
            print(*row)
        


        return dp[-1][-1]