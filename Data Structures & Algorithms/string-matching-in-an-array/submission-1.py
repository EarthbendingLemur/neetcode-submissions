class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        # guaranteed that len(w2) >= len(w1)
        def isSubsequence(w1, w2):
            L, R = 0, len(w1) - 1
            while R < len(w2):
                if w2[L:R + 1] == w1:
                    return True
                R += 1
                L += 1
            
            return False



        for i in range(len(words)):
            for j in range(len(words)):
                if i == j or len(words[i]) > len(words[j]):
                    continue
                
                if isSubsequence(words[i], words[j]):
                    res.append(words[i])

        return list(set(res))

