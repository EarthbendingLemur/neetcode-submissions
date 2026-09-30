class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hp = {}

        for i in range(26):
            hp[i] = 0

        for c in s:
            hp[ord(c) - ord('a')] += 1
        for c in t:
            hp[ord(c) - ord('a')] -= 1 
        
        for k,v in hp.items():
            if v != 0:
                return False
        
        return True