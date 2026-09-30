class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Whats in a palindrome
        # One odd char unique max
        # Every other char must be on even count

        mp = defaultdict(int)
        res = 0
        for c in s:
            mp[c] += 1
            if mp[c] % 2 == 0:
                res += 2
        
        for cnt in mp.values():
            if cnt % 2:
                res += 1
                break
        
        return res