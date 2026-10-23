class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        wq = [0] * len(words)

        def checkVowel(s):
            if s[0] in vowels and s[-1] in vowels:
                return True
            return False
        
        wq[0] = int(checkVowel(words[0]))
        for i in range(1, len(words)):
            wq[i] = checkVowel(words[i]) + wq[i - 1]
        res = []
        for l, r in queries:
            if l > 0:
                res.append(wq[r] - wq[l - 1])
            else:
                res.append(wq[r])

        return res

        
        


