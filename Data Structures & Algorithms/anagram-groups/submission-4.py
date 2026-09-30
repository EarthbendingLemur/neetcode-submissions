class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stored_words = {}

        for word in strs:
            word_arr = [0] * 26
            for letter in word:
                word_arr[ord(letter.lower()) - ord('a')] += 1
            word_tup = tuple(word_arr)
            if word_tup in stored_words:
                stored_words[word_tup].append(word)
            else:
                stored_words[word_tup] = [word] 
        
        return list(stored_words.values())
