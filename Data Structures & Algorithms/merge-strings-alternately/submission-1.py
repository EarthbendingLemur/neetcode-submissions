class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = ptr2 = 0
        sol = ""
        while ptr1 < len(word1) and ptr2 < len(word2):
            sol += word1[ptr1]
            sol += word2[ptr2]
            ptr1 += 1
            ptr2 += 1
        
        sol += word1[ptr1:]
        sol += word2[ptr2:]

        return sol
