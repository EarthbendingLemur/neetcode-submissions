class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        an_mp = {}

        for c in s:
            if c in an_mp:
                an_mp[c] += 1
            else:
                an_mp[c] = 1
        
        for c in t:
            if c not in an_mp:
                return False
            else:
                if an_mp[c] == 1:
                    del an_mp[c]
                else:
                    an_mp[c] -= 1
        
        return True