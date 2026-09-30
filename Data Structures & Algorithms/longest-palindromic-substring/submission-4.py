class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palindromeHelper(left, right):
            palindrome = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome = s[left:right + 1]
                left -= 1
                right += 1
            return palindrome
            

        res = ""
        for mid in range(len(s)):
            
            oddStr = palindromeHelper(mid, mid)
            evenStr = palindromeHelper(mid, mid + 1)

            if oddStr > evenStr and len(oddStr) > len(res):
                res = oddStr
            elif len(evenStr) > len(res):
                res = evenStr
            
        
        return res
