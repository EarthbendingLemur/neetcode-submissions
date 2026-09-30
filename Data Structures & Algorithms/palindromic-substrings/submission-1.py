class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        def palindromeWindow(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l = r = i
            palindromeWindow(l, r)
            l = i
            r = i + 1
            palindromeWindow(l, r)
        
        return res