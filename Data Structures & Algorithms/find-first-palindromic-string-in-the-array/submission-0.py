class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPal(s):
            L, R = 0, len(s) - 1

            while L <= R and s[L] == s[R]:
                L += 1
                R -= 1
            
            if L > R:
                return True
            return False
        

        
        for w in words:
            if isPal(w):
                return w
        
        return ""
