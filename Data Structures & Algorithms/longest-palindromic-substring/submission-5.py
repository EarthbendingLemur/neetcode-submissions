class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palHelper(L, R):
            res = ""
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res = s[L:R + 1]
                L -= 1
                R += 1
            return res
        
        res = ""
        for L in range(len(s)):
            odd = palHelper(L, L)
            even = palHelper(L, L + 1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even

        
        return res