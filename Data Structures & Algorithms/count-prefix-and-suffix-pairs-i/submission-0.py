class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixandSuffix(s1, s2):
            return s2.startswith(s1) and s2.endswith(s1)


        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixandSuffix(words[i], words[j]):
                    res += 1
        
        return res