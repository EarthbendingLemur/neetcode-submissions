class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        for i in range(26):
            charCount[i] = 0
        
        l, h = 0, 1
        charCount[ord(s[l]) - ord('A')] += 1
        max_length = 0
        
        while h < len(s):
            charCount[ord(s[h]) - ord('A')] += 1
            num_replacements = sum(charCount.values()) - max(charCount.values())
            if num_replacements > k:
                charCount[ord(s[l]) - ord('A')] -= 1
                print(l)
                l += 1
            h += 1
            max_length = max(max_length, h - l)
        
        return max_length