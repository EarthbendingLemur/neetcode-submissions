class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        sol = 0
        l,r = 0, 1

        if len(s) < 2:
            return len(s)
        seen.add(s[l])
        while r < len(s):

            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                sol = max(sol, r - l)
            else:
                seen.remove(s[l])
                l += 1
                


        return sol 
