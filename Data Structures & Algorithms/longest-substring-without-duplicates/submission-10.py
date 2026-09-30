class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        L, R = 0, 0
        res = 0
        while R < len(s):
            # Contract if in window
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            R += 1
            res = max(res, R - L)
        
        return res
