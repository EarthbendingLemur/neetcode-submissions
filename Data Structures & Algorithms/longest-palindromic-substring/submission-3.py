class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Imagine each point is the center of its palindrome
        # Move L, R pointers outwards from its center
        # Store longest palindrome as res
        # output res

        # Define a for loop outer
            # Define inner expanding palindromic window

        res = ""

        def palHelper(l, r):
            nonlocal res
            palindrome = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindrome = s[l:r + 1]
                l -= 1
                r += 1
            if len(palindrome) > len(res):
                res = palindrome
            
        for i in range(len(s)):
            L, R  = i, i
            palHelper(L, R)
            L, R = i, i + 1
            palHelper(L, R)

        

        return res



