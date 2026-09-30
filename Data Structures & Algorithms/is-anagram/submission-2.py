class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmp = {}
        for c in s:
            if c in hmp:
                hmp[c] = hmp[c] + 1
            else:
                hmp[c] = 1
        
        for c in t:
            if c not in hmp:
                return False
            else:
                hmp[c] = hmp[c] - 1
        
        for v in hmp.values():
            if v != 0:
                return False

        return True
        