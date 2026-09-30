class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)

        res = 0
        l, r = 0, 0

        while r < len(s):
            mp[s[r]] += 1
            # Check number of replacements required in the map
            # Contract window on conditional
            num_replace = sum(mp.values()) - max(mp.values())
            if num_replace > k:
                mp[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        

        return res