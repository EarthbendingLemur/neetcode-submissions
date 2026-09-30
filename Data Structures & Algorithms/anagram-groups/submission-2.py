class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alph_str = "abcdefghijklmnopqrstuvwxyz"

        alph:list = [0] * len(alph_str)
        
        hash_words = defaultdict(list)

        for word in strs:
            for letter in word:
                alph[alph_str.index(letter)] += 1
            
            hash_words[tuple(alph)].append(word)
            alph = [0] * len(alph_str)
            
        
        return list(hash_words.values())




        
        