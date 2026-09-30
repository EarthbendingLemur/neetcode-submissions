class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        res = 0
        charCount = {i:0 for i in range(26)}
        while R < len(s):
            charCount[ord(s[R]) - ord('A')] += 1
            num_replacements = sum(charCount.values()) - max(charCount.values())
            if num_replacements > k:
                charCount[ord(s[L]) - ord('A')] -= 1
                L += 1
            R += 1
            res = max(res, R - L)
        

        return res







