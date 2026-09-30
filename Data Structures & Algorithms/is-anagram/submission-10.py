class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}


        for c in s:
            if c in anagram:
                anagram[c] += 1
            else:
                anagram[c] = 1
        

        for c in t:
            if c in anagram:
                anagram[c] -= 1
                if anagram[c] == 0:
                    del anagram[c]
            else:
                return False
        
        return (len(anagram) == 0)

