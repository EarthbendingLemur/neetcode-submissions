
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        mp = {'a':0, 'b':0, 'c':0}
        for c in s:
            mp[c] += 1
        
        L = 0
        res = 0
        found = False
        if min(mp.values()) < k:
            return -1
        if k == 0:
            return 0
        
        for R in range(len(s)):
            mp[s[R]] -= 1
            
            while L < len(s) and min(mp.values()) < k:
                mp[s[L]] += 1
                L += 1
            res = max(res, R - L + 1)

        return len(s) - res

         