class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        l, r = 0, 0
        res = 0
        while r  < len(s):  
            if s[r] not in window:  
                window.add(s[r])
                r += 1
                res = max(res, len(window))
                continue
            window.remove(s[l])
            l += 1
        

        return res
            

            