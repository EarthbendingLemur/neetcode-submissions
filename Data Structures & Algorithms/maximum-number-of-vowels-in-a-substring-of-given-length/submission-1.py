class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        num_vowels = 0
        L = 0
        for R in range(k):
            if s[R] in vowels:
                num_vowels += 1
        res = num_vowels
        for R in range(k, len(s)):
            if s[R] in vowels:
                num_vowels += 1
            if s[L] in vowels:
                num_vowels -= 1
            L += 1
            res = max(res, num_vowels)

        return res
