class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        def pal_helper(l, r):
            nonlocal res
            palindrome = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindrome = s[l:r + 1] 
                l -= 1
                r += 1
            if len(palindrome) > len(res):
                res = palindrome
            
        for i in range(len(s)):
            # Send helper func for ODD length palindrome
            l = r = i
            pal_helper(l, r)
            # Send helper func for EVEN length palindrome
            l = i
            r = i + 1
            pal_helper(l, r)
    

        return res

