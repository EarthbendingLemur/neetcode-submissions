class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s) : 1}

        def backtrack(idx):
            if idx in dp:
                return dp[idx]
                       
            if s[idx] == '0':
                return 0
            
            res = backtrack(idx + 1)

            if idx < len(s) - 1:
                if (s[idx] == '1' or (s[idx] == '2' and s[idx + 1] < '7')):
                    res += backtrack(idx + 2)
            
            dp[idx] = res
            return res
        
        return backtrack(0)