class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_m = {}
        
        for c in s:
            if c in s_m:
                s_m[c] += 1
            else:
                s_m[c] = 1
        
        for c in t:
            if c not in s_m:
                return False
            else:
                if s_m[c] == 1:
                    del s_m[c]
                else:
                    s_m[c] -= 1
        
        return not s_m