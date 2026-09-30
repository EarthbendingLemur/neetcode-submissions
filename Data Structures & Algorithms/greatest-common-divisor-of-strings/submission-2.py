class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        
        def divides(s, t):
            while s[:len(t)] == t:
                s = s[len(t):]
            
            return s == ""

        for i in range(len(str2)):
            ans = str2[:i + 1]
            if divides(str1, ans) and divides(str2, ans):
                res = ans
        
        return res

