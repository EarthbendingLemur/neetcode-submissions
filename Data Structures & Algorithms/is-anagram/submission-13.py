class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord("a")] += 1
        for c in t:
            letters[ord(c) - ord("a")] -= 1
        
        for l in letters:
            if not l == 0:
                return False
        return True
