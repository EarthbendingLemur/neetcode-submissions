class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        num_replacements = 0
        mp_window = defaultdict(int)
        res = 0
        while R < len(s):
            mp_window[s[R]] += 1
            num_replacements = sum(mp_window.values()) - max(mp_window.values())
            while num_replacements > k:
                mp_window[s[L]] -= 1
                num_replacements = sum(mp_window.values()) - max(mp_window.values())
                L += 1
            res = max(res, R - L + 1)
            R += 1

        return res
        
