class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = {}
        for i in range(26):
            mp[i] = 0
        
        for c in s:
            mp[ord(c) - ord('a')] += 1
        
        for c in t:
            mp[ord(c) - ord('a')] -= 1
        

        for k, v in mp.items():
            if v != 0:
                return chr(k + ord('a'))
        
        return ""