class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        rep = [0] * 26

        for c in s:
            rep[ord(c) - ord('a')] += 1
        
        for c in t:
            rep[ord(c) - ord('a')] -= 1

        
        for v in rep:
            if v != 0:
                return False
        
        return True


