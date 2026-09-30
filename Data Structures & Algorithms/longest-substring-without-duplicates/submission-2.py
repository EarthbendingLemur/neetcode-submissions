class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        if len(s) < 2:
            return len(s)
        res = s[l]
        max_res = len(res)
        while r < len(s):
            if s[r] in res:
                l += 1
                res = res[1:]
            else:
                res += s[r]
                r += 1 
            max_res = max(max_res, len(res))
        return max_res